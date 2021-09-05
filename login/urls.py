from django.urls import path
from login.views import *

urlpatterns = [
                path('', index),
                path('success', success),
                path('logout', logout),
                path('login/process', process_login),
                path('register/process', process_register),
                path('api/login/validate_email/<str:email>', validate_email)
              ]
