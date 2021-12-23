from django.shortcuts import render, get_object_or_404, redirect
import requests
from  .models import City
from .forms import CityForm

# Create your views here.

def weather(request):
    API_id = '8389fc42da1b139fd4399f3ef77b3833'
    url= 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_id
    
    if (request.method == 'POST'):
        form=CityForm(request.POST)
        form.save()
    
    form=CityForm()

    cities=City.objects.all()
    all_cities=[]

    for city in cities:
        res=requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/weather.html', context)
