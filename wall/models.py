from django.db import models
from login.models import User

# Create your models here.
class Message(models.Model):
    user_id    = models.ForeignKey(User, on_delete=models.CASCADE)
    text       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='comments')
    user_id    = models.ForeignKey(User,    on_delete=models.CASCADE)
    text       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
