from django.urls import path
from login.views import *

urlpatterns = [
                path('', index),
                path('login/process', process_login),
                path('register/process', process_register)
              ]
