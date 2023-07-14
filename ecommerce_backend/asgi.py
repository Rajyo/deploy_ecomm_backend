"""
ASGI config for ecommerce_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
from ecommerce_backend.settings import *
import os

from django.core.asgi import get_asgi_application

if DEBUG == True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings_rail')

application = get_asgi_application()
