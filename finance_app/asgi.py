"""
ASGI config for finance_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_app.settings')

application = get_asgi_application()
