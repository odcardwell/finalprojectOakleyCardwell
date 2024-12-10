# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.products import Products
from plaid.model.country_code import CountryCode

import json
import logging
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import PlaidAccount
from .utils import client
from transactions.models import Transaction, Category

from plaid.exceptions import ApiException
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions

@login_required
def get_link_token(request):
    try:
        # Construct the request payload
        request_data = LinkTokenCreateRequest(
            products=[Products('transactions')],
            client_name='FinanceTool',
            country_codes=[CountryCode('US')],
            language='en',
            user={'client_user_id': str(request.user.id)}
        )
        # Call Plaid API to create a link token
        response = client.link_token_create(request_data)
        link_token = response.to_dict()['link_token']
        return JsonResponse({'link_token': link_token})
    except ApiException as e:
        error_response = json.loads(e.body)
        logger.error(f"Error creating link token: {error_response.get('error_message')}")
        return JsonResponse({'error': error_response.get('error_message')})

@csrf_exempt
@login_required
def exchange_public_token(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        public_token = data.get('public_token')
        try:
            # Use the imported class to create the request object
            exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
            # Call the Plaid API
            exchange_response = client.item_public_token_exchange(exchange_request)
            # Extract the access token and item ID
            access_token = exchange_response.access_token
            item_id = exchange_response.item_id
            # Save to the database
            PlaidAccount.objects.create(
                user=request.user,
                access_token=access_token,
                item_id=item_id,
                institution_name='',  # Update with institution details if needed
            )
            return JsonResponse({'status': 'success'})
        except ApiException as e:
            error_response = json.loads(e.body)
            logger.error(f"Error exchanging public token: {error_response.get('error_message')}")
            return JsonResponse({'status': 'error', 'message': error_response.get('error_message')})
        except Exception as e:
            logger.exception("An unexpected error occurred during token exchange.")
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

logger = logging.getLogger(__name__)

@login_required
def fetch_transactions(request):
    plaid_accounts = PlaidAccount.objects.filter(user=request.user)
    if not plaid_accounts.exists():
        messages.error(request, 'No linked bank accounts found.')
        return redirect('transactions:transaction_list')
    for account in plaid_accounts:
        start_date = (datetime.now() - timedelta(days=30)).date()
        end_date = datetime.now().date()
        transactions = []
        total_transactions = 0
        offset = 0
        try:
            while True:
                options = TransactionsGetRequestOptions(count=100, offset=offset)
                request_data = TransactionsGetRequest(
                    access_token=account.access_token,
                    start_date=start_date,
                    end_date=end_date,
                    options=options
                )
                response = client.transactions_get(request_data)
                transactions.extend(response.transactions)
                total_transactions = response.total_transactions
                if len(transactions) >= total_transactions:
                    break
                offset += len(response.transactions)
            # Process and save transactions
            for txn in transactions:
                logger.debug(f"Processing transaction: {txn.name}, Amount: {txn.amount}, Date: {txn.date}")
                # Check if transaction already exists
                if not Transaction.objects.filter(
                    user=request.user,
                    date=txn.date,
                    amount=abs(txn.amount),
                    description=txn.name
                ).exists():
                    # Get or create category
                    category_name = txn.category[0] if txn.category else 'Uncategorized'
                    category, _ = Category.objects.get_or_create(user=request.user, name=category_name)
                    # Determine transaction type and amount based on observed behavior
                    if txn.amount > 0:
                        transaction_type = 'expense'
                        amount = txn.amount
                    else:
                        transaction_type = 'income'
                        amount = abs(txn.amount)
                    # Create Transaction
                    Transaction.objects.create(
                        user=request.user,
                        amount=amount,
                        date=txn.date,
                        category=category,
                        transaction_type=transaction_type,
                        description=txn.name,
                    )
            messages.success(request, 'Transactions fetched successfully.')
        except ApiException as e:
            error_response = json.loads(e.body)
            error_message = error_response.get('error_message', 'An error occurred with Plaid API.')
            logger.error(f"Plaid API Error: {error_message}")
            messages.error(request, f"Error fetching transactions: {error_message}")
        except Exception as e:
            logger.exception("An unexpected error occurred while fetching transactions.")
            messages.error(request, f"An unexpected error occurred: {str(e)}")
    return redirect('transactions:transaction_list')

@login_required
def link_account(request):
    return render(request, 'plaid_integration/link_account.html')



