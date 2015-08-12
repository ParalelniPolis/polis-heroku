from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def currently_playing(request):
    return HttpResponse('ok')
