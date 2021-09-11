from django.http import JsonResponse
from wall import data

# Create your views here.
def message_post(request):
    return JsonResponse(data.message_post(request))


def message_delete(request):
    return JsonResponse(data.message_delete(request))


def comment_post(request):
    return JsonResponse(data.comment_post(request))


def comment_delete(request):
    return JsonResponse(data.comment_delete(request))
