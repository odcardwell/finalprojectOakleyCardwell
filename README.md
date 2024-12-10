# FinanceTool
### INF601 Advanced Programming with Python
### Oakley Cardwell

## Project Description
This project is a Django-based web application designed to help users manage their personal finances effectively. It integrates with external financial APIs (like Plaid) to automatically fetch and categorize transactions from linked bank accounts. Users can view and manage their budgets, track financial goals, review transaction histories (both manual and fetched from Plaid), and gain insights into their spending habits. The application demonstrates database integration, user authentication, secure data handling, and a responsive UI with Bootstrap enhancements.

## Application Features
- User Authentication: Secure registration and login system using Django's built-in authentication framework.
- Transaction Management: Fetch and process transactions from linked bank accounts via Plaid. Users can also manually add, edit, or delete transactions.
- Budgets: Set up budgets for different categories and time spans. Monitor financial goals and track progress over time.
- Category Management: Organize and categorize expenses and income for clearer financial insights.
- Responsive Interface with Bootstrap: A clean and mobile-friendly UI, enhanced with Bootstrap styles, responsive layouts, and optional animations for a polished user experience.
- Database Integration: Uses SQLite (by default) for data storage, with models for transactions, budgets, categories, goals, and linked accounts. 

## Understanding the Application
Upon launching the application, users can:

- Link Accounts: Securely connect their bank accounts via Plaid for automatic transaction imports.
- View Transactions: Browse fetched and manually-added transactions. Transactions are displayed with categories and types (income or expense).
- Manage Budgets and Goals: Set budgets for specific periods and categories. Track financial goals to maintain financial health and spending discipline.
- Adjust Categories and Performances: Review categories, reassign transactions, and refine categories to align with personal needs.
- User Authentication: Register and log in to access personalized financial data. Logged-in users can view and modify their data securely.
- Admin Interface: Access the Django admin site to manage models like categories, budgets, and transactions.

## Installation
### Clone the Repository:

```bash
git clone https://github.com/odcardwell/finalprojectOakleyCardwell.git
```

### Navigate to the Project Directory:

```bash
cd finalprojectOakleyCardwell
```
### Create a Virtual Environment:


```bash
python -m venv venv
```

### Activate the Virtual Environment:

On Windows:

```bash
venv\Scripts\activate
```

### Install the Required Dependencies:

```bash
pip install -r requirements.txt
```

## Database Initialization
Before running the application, you need to set up the database.

### Make Migrations:

```bash
python manage.py makemigrations
```
### Apply Migrations:

```bash
python manage.py migrate
```

### Create a Superuser (for Admin Access):

```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

## Running the Development Server
### Run the Django Application:

```bash
python manage.py runserver
```

### Access the Application:

Open a web browser and navigate to http://127.0.0.1:8000/ to view the application.


## Requirements
`requirements.txt` contains the necessary dependencies for the project.
You can generate the requirements file by running:

```bash
pip freeze > requirements.txt
```

## Notes
- API Integration (Plaid): Make sure you have valid Plaid API credentials and set them in the application's settings.

- Media and Static Files: Configure MEDIA_URL and MEDIA_ROOT if you store images or files. Static files are managed through Django's static file system.

- Security Considerations: Use unique, secret keys in settings.py, and consider additional security settings when deploying to production.

- Production Deployment: For live environments, use a production server (like Gunicorn/Nginx), configure ALLOWED_HOSTS, and enable HTTPS.

## Conclusion
This finance tool application showcases essential web development skills with Django, from model design and authentication to external API integration and responsive UI design. By following the installation and usage instructions, you can explore, test, and extend the application's capabilities to better understand personal finance management and Django-based web applications.