from django.contrib import messages
from django.shortcuts import render, redirect

from datetime import datetime

from login.models import User
from wall.models import Message, Comment
from wall import data


# Create your views here.
def index(request):
    context = data.index(request)
    print(context)
    return render(request, 'wall.html', context)


def message_post(request):
    response = data.message_post(request)
    print(response)
    if not response['success']:
        messages.error(request, response.error)
    return redirect('/wall')


def message_delete(request):
    response = data.message_delete(request)
    print(response)
    if not response['success']:
        messages.error(request, response.error)
    return redirect('/wall')


def comment_post(request):
    response = data.comment_post(request)
    print(response)
    if not response['success']:
        messages.error(request, response.error)
    return redirect('/wall')

def comment_delete(request):
    response = data.comment_delete(request)
    print(response)
    if not response['success']:
        messages.error(request, response.error)
    return redirect('/wall')
