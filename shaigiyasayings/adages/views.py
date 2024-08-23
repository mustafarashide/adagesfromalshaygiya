from django.shortcuts import render
from django.http import HttpResponse
import random #when going to index view -> send user to a random adage
# Create your views here.

def index(request):
    return detail(request,random.random())
def detail(request,adage_id):
    response = "You're looking at adage %s."
    return HttpResponse(response % adage_id)