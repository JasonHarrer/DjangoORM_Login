from django.urls import path
from wall import views

urlpatterns = [
                path('', views.index),
                path('message/post', views.message_post),
                path('message/delete', views.message_delete)
              ]
