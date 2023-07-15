"""
WSGI config for ecommerce_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
from ecommerce_backend.settings import *
import os

from django.core.wsgi import get_wsgi_application

# if DEBUG == True:
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings')
# else:
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings_rail')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings')

application = get_wsgi_application()
