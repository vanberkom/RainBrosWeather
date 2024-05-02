from django.shortcuts import render
import requests
from datetime import datetime
from datetime import date
from . import zipToCord

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
                        current_time = datetime.now()
                        current_hour = current_time.hour
                        current_hour = current_hour - 17
                        hourly_time1 = str(current_hour) + ":00"
                        hourly_time2 = str(current_hour + 1) + ":00"
                        hourly_time3 = str(current_hour + 2) + ":00"
                        hourly_time4 = str(current_hour + 3) + ":00"
                        hourly_time5 = str(current_hour + 4) + ":00"
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
                    c2 = {
                        'city': city,
                        'temperature': temperature,
                        'date': todays_date,
                    }
                    context = context | c2
                    
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
