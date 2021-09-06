from django.db import models
from django.utils.dateparse import parse_date
from datetime import date

# Create your models here.
class UserManager(models.Manager):
    def validate(self, POST):
        errors = {}
        
        if not POST['register_first_name']:
            errors['register_first_name_missing'] = 'A first name is required.'
        if not POST['register_last_name']:
            errors['register_last_name_missing'] = 'A last name is required.'
        if not POST['register_email']:
            errors['register_email_missing'] = 'An email addres is required.'
        if not POST['register_birthdate']:
            errors['register_birthdate_missing'] = 'A birth date is required.'
        elif parse_date(POST['register_birthdate']) > date.today().replace(year=date.today().year - 13):
            errors['register_birthdate_too_young'] = 'You must be 13 years of age or older to create an account on this website.'
        if not POST['register_password1'] or not POST['register_password2']:
            errors['register_password_missing'] = 'Password must be entered twice and they must match.'
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.CharField(max_length=255)
    password   = models.CharField(max_length=100)
    birthdate  = models.DateField()
    objects    = UserManager()
