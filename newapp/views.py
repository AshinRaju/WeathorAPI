import json
import urllib

from django.shortcuts import render


def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=73d030ee27e048386b0f861aae55ecf0'
        source = urllib.request.urlopen(url).read()
        data = json.loads(source)
        r = data["main"]["temp"]
        temp = round(r - 273.15)
        weather_data = {
            "city": city,
            "country_code": str(data['sys']['country']),
            "coordinate": str(data['coord']['lon']) + ' ' + str(data['coord']['lat']),
            "temp": temp,
            "pressure": str(data['main']['pressure']),
            "humidity": str(data['main']['humidity']),
        }
    else:
        weather_data = {}

    return render(request,'index.html',weather_data)
