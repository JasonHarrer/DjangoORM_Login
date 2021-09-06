from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render, redirect
from bcrypt import hashpw, gensalt, checkpw
from datetime import date

from login.models import *

# Create your views here.
def index(request):
    context = {
                'source': request.session['source'] if 'source' in request.session else None,
                'today':  date.today().isoformat()
              }
    return render(request, 'index.html', context)


def process_login(request):
    # Add source for login for messages checking
    request.session['source'] = request.POST['source']
    try:
        user = User.objects.get(email=request.POST['login_email'])
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist exception')
        messages.error(request, 'Invalid Username and/or Password')
        return redirect('/')
    if checkpw(request.POST['login_password'].encode(), user.password.encode()):
        print('email/password check successful')
        request.session['userid'] = user.id
        return redirect('/success')
    else:
        print('email/password check failed')
        messages.error(request, 'Invalid Username and/or Password')
        return redirect('/')
        


def process_register(request):
    request.session['source'] = request.POST['source']
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
            return redirect('/')
    else:
        user = User.objects.create(
                                    first_name = request.POST['register_first_name'],
                                    last_name  = request.POST['register_last_name'],
                                    birthdate  = request.POST['register_birthdate'],
                                    email      = request.POST['register_email'],
                                    password   = hashpw(
                                                         request.POST['register_password1'].encode(),
                                                         gensalt()
                                                       ).decode()
                           )
        if user:
            request.session['userid'] = user.id
        return redirect('/success')


def success(request):
    if 'userid' not in request.session:
        raise PermissionDenied
    
    try:
        user = User.objects.get(id=request.session['userid'])
    except ObjectDoesNotExist:
        raise PermissionDenied
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
