from django.shortcuts import render
from django.http import HttpResponse
from .models import Adage
import json


# Create your views here.

def home_view(request):
    return render(request,'base.html') 

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
