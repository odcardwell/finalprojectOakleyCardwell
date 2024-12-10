"""
WSGI config for finance_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_app.settings')

application = get_wsgi_application()
