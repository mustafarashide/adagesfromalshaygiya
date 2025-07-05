from django.shortcuts import render
from django.http import HttpResponse
from .models import Adage
import json
import random


# Create your views here.

def home_view(request):
    number_of_adages = Adage.objects.count()
    random_adage=Adage.objects.all()[random.randrange(0,number_of_adages)]
    return render(request,'base.html',{"random_adage":random_adage}) 

'''
def import_data(request):
    """
    takes an adages json string and creates adage
    """
    if request.method == 'POST' and request.FILES['json_file']:
        json_file = request.FILES['json_file']
        data = json.load(json_file)
        for item in data:
            adage = Adage(
                    adage_id = item['id'],
                    adage_text = item['adage_text'],
                    adage_meaning = item['adage_meaning'],
                    review_status = False
                    )
            adage.save()
'''
