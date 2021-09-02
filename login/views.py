from django.shortcuts import render
from login.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def process_login(request):
    pass


def process_register(request):
    pass
