from django.core import serializers
from django.utils import timezone
from datetime import timedelta
from login.models import *
from wall.models import *


def index(request):
    wall_comments = {}
    wall_messages = Message.objects.all().order_by('-created_at')
    for message in wall_messages:
        wall_comments[message.id] = Comment.objects.filter(message_id = message.id).order_by('created_at')
    data = {
             'user':          User.objects.get(id=request.session['userid']),
             'wall_messages': wall_messages,
             'wall_comments': wall_comments,
             'delete_time':   timezone.now() - timedelta(minutes=30)
           }
    return data


def message_post(request):
    user = User.objects.get(id=request.session['userid'])
    message = Message.objects.create(
                                      user_id = user,
                                      text    = request.POST['message_text']
                                    )
    return {
             'success': True,
             'author':  UserSerializer(instance=user).data,
             'message': MessageSerializer(instance=message).data
           }


def message_delete(request):
    message = Message.objects.get(id=request.POST['message_id'])
    if request.session['userid'] == message.user_id.id:
        print(f'message delta: {message.created_at + timedelta(minutes=30)}\nCurrent timezone time: {timezone.now()}')
        if (message.created_at + timedelta(minutes=30) >= timezone.now()):
            message.delete()
            return { 'success': True }

        return {
                 'success': False,
                 'error':  'Message was created more than 30 minutes ago.  You can no longer delete this message.'
               }
    return {
             'success': False,
             'error':   'Only the author of this message may delete this message.'
           }


def comment_post(request):
    user = User.objects.get(id=request.session['userid'])
    message = Message.objects.get(id=request.POST['message_id'])

    comment = Comment.objects.create(
                                      message_id = message,
                                      user_id    = user,
                                      text       = request.POST['comment_text']
                                    )
    return {
             'success': True,
             'id':      serialize('json', comment)
           }


def comment_delete(request):
    comment = Comment.objects.get(id=request.POST['comment_id'])
    if request.session['userid'] == comment.user_id.id:
        comment.delete()
        return { 'success': True }
    return {
             'success': False,
             'error':   'Only the author of this comment may delete this comment.'
           }
