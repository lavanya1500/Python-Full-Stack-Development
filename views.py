from django.shortcuts import render
from .models import MyModel
from django.http import HttpResponse
import json

def database(request):
    data= MyModel.objects.all()
    serialized_data= json.dumps([{
        'sector': entry.sector,
        'intensity': entry.intensity,
        'likelihood':entry.likelihood,
        'relevance':entry.relevance,
        'start_year':entry.start_year,
        'end_year':entry.end_year,
        'country':entry.country,
        'topic':entry.topic,
        'region':entry.region,
        'insight':entry.insight
    } for entry in data])
    return render(request, 'body.html', {'serialized_data':serialized_data})