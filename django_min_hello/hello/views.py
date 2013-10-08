from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hi from Django (without middleware)")
