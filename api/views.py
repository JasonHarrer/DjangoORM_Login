from django.http import JsonResponse
from wall import data

# Create your views here.
def message_post(request):
    response = data.message_post(request)
    print(f'Response:  {response}')
    return JsonResponse(response, safe=False)
    #return JsonResponse(data.message_post(request))


def message_delete(request):
    response = data.message_delete(request)
    print(response)
    return JsonResponse(response)
    #return JsonResponse(data.message_delete(request))


def comment_post(request):
    response = data.comment_post(request)
    print(response)
    return JsonResponse(response)
    #return JsonResponse(data.comment_post(request))


def comment_delete(request):
    response = data.comment_delete(request)
    print(response)
    return JsonResponse(response)
    #return JsonResponse(data.comment_delete(request))
