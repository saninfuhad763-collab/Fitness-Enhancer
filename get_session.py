"""
Generate a valid Django session cookie for freeuser, then pass it to Playwright.
"""
import os, django, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from users.models import Subscription

# Ensure freeuser exists and is free
free_user, _ = User.objects.get_or_create(username='freeuser')
Subscription.objects.update_or_create(user=free_user, defaults={'plan': 'free'})

c = Client()
c.force_login(free_user)

# Get the session cookie value
session_key = c.session.session_key
print(f"SESSION_KEY={session_key}")
