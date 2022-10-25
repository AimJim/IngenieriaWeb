from http.client import HTTPResponse
from django.http import HttpResponse

def index(request):
    return HttpResponse("Resuesta del index")
