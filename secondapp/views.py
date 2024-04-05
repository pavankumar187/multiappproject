from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish2(request):
    return HttpResponse('<h2> this is secondapp</h2>')
