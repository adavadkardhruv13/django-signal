from django.urls import path
from .views import create_user, check_thread, check_db

urlpatterns = [
    path('create-user/', create_user, name='create_user'),
    path('check_thread/', check_thread, name='check_thread'),
    path('check_db/', check_db, name='check_db'),
]
