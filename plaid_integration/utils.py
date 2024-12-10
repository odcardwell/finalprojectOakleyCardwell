# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

import plaid
from plaid.api import plaid_api
from django.conf import settings

# Set up the Plaid client configuration
configuration = plaid.Configuration(
    host=plaid.Environment.Production if settings.PLAID_ENV == 'production' else
         plaid.Environment.Development if settings.PLAID_ENV == 'development' else
         plaid.Environment.Sandbox,
    api_key={
        'clientId': settings.PLAID_CLIENT_ID,
        'secret': settings.PLAID_SECRET,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)


