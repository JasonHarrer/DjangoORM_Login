from django.urls import path
from api.views import *

urlpatterns = [
                path('message/post',   message_post),
                path('message/delete', message_delete),
                path('comment/post',   comment_post),
                path('comment/delete', comment_delete)
              ]
