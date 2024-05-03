from django.shortcuts import render
import requests
from datetime import datetime
from datetime import date
from . import zipToCord,timeFormat

# Create your views here.
def index(request):
    context={}
    return render(request, 'index.html', context=context)

def errorpage(request):
    return render(request, 'error.html', context={})

def daily(request):
    zip_code = request.GET.get('zipcode', None)
    context={}
    if zip_code:
        city, lat, lon = zipToCord.ZipToCity(zip_code)
        
        if lat and lon and city:
            input_url = f'https://api.weather.gov/points/{lat},{lon}'
            forecast_url = ''
            
            response = requests.get(input_url)
            
            if response.status_code == 200:
                data = response.json()
                forecast_url = data['properties']['forecast']
                hourly_url = data['properties']['forecastHourly']
                response = requests.get(forecast_url)
                
                if response.status_code == 200:
                    
                    results = response.json()
                    temperature = results['properties']['periods'][0]['temperature']
                    
                    today = date.today()
                    todays_date = today.strftime('%A, %B %d')
                    
                    response = requests.get(hourly_url)
                    if response.status_code == 200:
                        results = response.json()

                        # Getting api hourly data
                        hourly_temp1 = results['properties']['periods'][0]['temperature']
                        hourly_pic1 = results['properties']['periods'][0]['icon']
                        hourly_wind1 = results['properties']['periods'][0]['windSpeed']
                        hourly_winddir1 = results['properties']['periods'][0]['windDirection']
                        hourly_temp2 = results['properties']['periods'][1]['temperature']
                        hourly_pic2 = results['properties']['periods'][1]['icon']
                        hourly_wind2 = results['properties']['periods'][1]['windSpeed']
                        hourly_winddir2 = results['properties']['periods'][1]['windDirection']
                        hourly_temp3 = results['properties']['periods'][2]['temperature']
                        hourly_pic3 = results['properties']['periods'][2]['icon']
                        hourly_wind3 = results['properties']['periods'][2]['windSpeed']
                        hourly_winddir3 = results['properties']['periods'][2]['windDirection']
                        hourly_temp4 = results['properties']['periods'][3]['temperature']
                        hourly_pic4 = results['properties']['periods'][3]['icon']
                        hourly_wind4 = results['properties']['periods'][3]['windSpeed']
                        hourly_winddir4 = results['properties']['periods'][3]['windDirection']
                        hourly_temp5 = results['properties']['periods'][4]['temperature']
                        hourly_pic5 = results['properties']['periods'][4]['icon']
                        hourly_wind5 = results['properties']['periods'][4]['windSpeed']
                        hourly_winddir5 = results['properties']['periods'][4]['windDirection']
                        
                        # Finding time
                        current_time = datetime.now().hour
                        hourly_time1, hourly_time2, hourly_time3, hourly_time4, hourly_time5 = timeFormat.timeFormatter(current_time)
                        hourly_time1 = str(hourly_time1 + 1) + ":00"
                        hourly_time2 = str(hourly_time1 + 2) + ":00"
                        hourly_time3 = str(hourly_time1 + 3) + ":00"
                        hourly_time4 = str(hourly_time1 + 4) + ":00"
                        hourly_time5 = str(hourly_time1 + 5) + ":00"
                        # Filling Django Variables
                        context = {
                            'hourly_time1': hourly_time1,
                            'hourly_temp1': hourly_temp1,
                            'hourly_pic1': hourly_pic1,
                            'hourly_wind1': hourly_wind1,
                            'hourly_winddir1': hourly_winddir1,
                            'hourly_time2': hourly_time2,
                            'hourly_temp2': hourly_temp2,
                            'hourly_pic2': hourly_pic2,
                            'hourly_wind2': hourly_wind2,
                            'hourly_winddir2': hourly_winddir2,
                            'hourly_time3': hourly_time3,
                            'hourly_temp3': hourly_temp3,
                            'hourly_pic3': hourly_pic3,
                            'hourly_wind3': hourly_wind3,
                            'hourly_winddir3': hourly_winddir3,
                            'hourly_time4': hourly_time4,
                            'hourly_temp4': hourly_temp4,
                            'hourly_pic4': hourly_pic4,
                            'hourly_wind4': hourly_wind4,
                            'hourly_winddir4': hourly_winddir4,
                            'hourly_time5': hourly_time5,
                            'hourly_temp5': hourly_temp5,
                            'hourly_pic5': hourly_pic5,
                            'hourly_wind5': hourly_wind5,
                            'hourly_winddir5': hourly_winddir5,
                        }
                    # Adding city variables to django context
                    c2 = {
                        'city': city,
                        'temperature': temperature,
                        'date': todays_date,
                    }
                    # Combining the contexts
                    context = context | c2
                    # Rendering the daily html with the information
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
