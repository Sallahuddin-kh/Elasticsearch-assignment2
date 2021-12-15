from django.shortcuts import render
import requests
from requests.exceptions import ConnectionError,HTTPError,Timeout,TooManyRedirects
import json
from elasticsearch import Elasticsearch

# Create your views here.

def civilizations(request):
    response_data = requests.get("https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations")
    return_list = response_data.json()
    civilization_list = return_list['civilizations']
    es = Elasticsearch()
    for oo in civilization_list:
        res = es.index(index="civilizations", body=oo)
    return render(request, 'ageofempires/civilizations.html' )