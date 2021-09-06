from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from login.models import User
from wall.models import Message, Comment


# Create your views here.
def index(request):
    data = {
             'wall_messages': Message.objects.all().order_by('-created_at'),
             'user':          User.objects.get(id=request.session['userid'])
           }
    return render(request, 'wall.html', data)


def message_post(request):
    user = User.objects.get(id=request.session['userid'])
    Message.objects.create(
                            user_id = user,
                            text    = request.POST['message_text']
                          )
    return redirect('/wall')


def message_delete(request):
    message = Message.objects.get(id=request.POST['message_id'])
    print(f'Message User ID: {message.user_id.id}\t\tLogged In User Id: {request.session["userid"]}')
    if request.session['userid'] == message.user_id.id:
        message.delete()
        return redirect('/wall')
    else:
        raise PermissionDenied
