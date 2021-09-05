from django.http import JsonResponse
from django.shortcuts import render, redirect
from bcrypt import hashpw, gensalt

from login.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def process_login(request):
    pass


def process_register(request):
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
            return redirect('/')
    else:
        with request.POST as POST:
            User.objects.create(
                                 first_name = POST['registration_first_name'],
                                 last_name  = POST['registration_last_name'],
                                 email      = POST['registration_email'],
                                 password   = hashpw(
                                                      POST['password1'].encode(),
                                                      gensalt()
                                                    ).decode()
                               )

def validate_email(request):
    response = JsonResponse({ 
                              'exists': (User.objects.filter(email=request.POST['email']).count() > 1)
                            })
