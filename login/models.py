from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, POST):
        errors = {}
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.CharField(max_length=255)
    password   = models.CharField(max_length=100)
