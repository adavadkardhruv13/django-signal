from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
import threading
from django.db import transaction

# Create your views here.

# so this view work in a way that when we create a user it hits the signal function(sync_signal) saved in signals.py which tells us that 
# the django signal works synchronously by default

def create_user(request):
    user = User.objects.create(username='test_usern', email='test1@example.com')
    return JsonResponse({"message": "User created successfully!"})

#-------------------------------------------------------------------------------------------------

# so this view work in an way that it tell that the django signal works in the same thread as that of the caller
# so this first show the caller thread number and then the signal's thread number

def check_thread(request):
    print(f"[VIEW] Running in thread: {threading.get_ident()}")
    user = User.objects.create(username='test_3', email='test1@example.com')
    return JsonResponse({"message": "User created successfully!"})

#-------------------------------------------------------------------------------------------------

# this view work in a way that it shows that the django signals run in the same database transaction as the caller
# this is done by showing that when the user is created and then an exception comes that rollbacks the db_transation saying user_exists : False
# which means that django signals run in the same database transaction as the caller

def check_db(request):
    try:
        with transaction.atomic():  # Start transaction
            print("[VIEW] Creating user...")
            user = User.objects.create(username="test1", email="test@example.com")
            print("[VIEW] User created successfully!")
    except Exception as e:
        print(f"[VIEW] Exception caught: {e}")
    
    user_exists = User.objects.filter(username="test1").exists()
    return JsonResponse({"user_exists": user_exists})
