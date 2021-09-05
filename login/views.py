from django.contrib import messages
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
        user = User.objects.create(
                                    first_name = request.POST['register_first_name'],
                                    last_name  = request.POST['register_last_name'],
                                    email      = request.POST['register_email'],
                                    password   = hashpw(
                                                         request.POST['register_password1'].encode(),
                                                         gensalt()
                                                       ).decode()
                           )
        if user:
            request.session['userid'] = user.id
            request.session['source'] = request.POST['source']
        return redirect('/success')


def success(request):
    context = {
                'user':  User.objects.get(id=request.session['userid']),
                'source': request.session['source']
              }
    return render(request, 'success.html', context)


def logout(request):
    try:
        del request.session['userid']
        del request.session['source']
    except KeyError:
        pass
    return redirect('/')


def validate_email(request, email):
    response = JsonResponse({ 
                              'exists': (User.objects.filter(email=email).count() > 1)
                            })
    return response
