from django.shortcuts import render
import requests
import json
from datetime import date
from . import zipToCord

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context=context)

def errorpage(request):
    return render(request, 'error.html', context={})

def daily(request):
    zip_code = request.GET.get('zipcode', None)
    
    if zip_code:
        city, lat, lon = zipToCord.ZipToCity(zip_code)
        
        if lat and lon and city:
            input_url = f'https://api.weather.gov/points/{lat},{lon}'
            forecast_url = ''
            
            response = requests.get(input_url)
            
            if response.status_code == 200:
                data = response.json()
                forecast_url = data['properties']['forecast']
                response = requests.get(forecast_url)
                
                if response.status_code == 200:
                    results = response.json()
                    temperature = results['properties']['periods'][0]['temperature']

                    
                    today = date.today()
                    todays_date = today.strftime('%A, %B %d')
                    
                    context = {
                        'city': city,
                        'temperature': temperature,
                        'date': todays_date,
                    }
                    
                    return render(request, 'daily.html', context=context)
                
                else:
                    return render(request, 'error.html', context={})
            
            else:
                return render(request, 'error.html', context={})
        
        else:
            return render(request, 'error.html', context={})
    
    else:
        return render(request, 'error.html', context={})

def weekly(request):
    return render(request, 'weekly.html', context={})

def affirmation(request):
    try:
        response = requests.get('https://zenquotes.io/api/random')
        data = response.json()
        quote = data[0]['q']  # Quote text
        author = data[0]['a']  # Author of the quote
    except Exception as e:
        quote = "No affirmation available at the moment."
        author = ""
        print(f"API request failed: {e}")
    return render(request, 'affirmation.html', {'quote': quote})



def affirmation(request):
    try:
        response = requests.get('https://zenquotes.io/api/random')
        data = response.json()
        quote = data[0]['q']  # Quote text
        author = data[0]['a']  # Author of the quote
    except Exception as e:
        quote = "No affirmation available at the moment."
        author = ""
        print(f"API request failed: {e}")
    return render(request, 'affirmation.html', {'quote': quote})