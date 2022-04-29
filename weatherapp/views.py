from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':            # making post request to API
        city = request.POST['city']         # city name whose weather is to be determined
        source = requests.get('http://api.openweathermap.org/data/2.5/weather?q='
                                        + city + '&units=metric&appid=c684623cf9b9f3de994dca79291a6f35')
                                            # source contains all the data from the API
        list_of_data = source.json()        # to convert json data into python dictionary
        data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ', '
                      + str(list_of_data['coord']['lat']),

        "temp": str(list_of_data['main']['temp']) + ' °C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        'main': str(list_of_data['weather'][0]['main']),
        'description': str(list_of_data['weather'][0]['description']),
        'icon': list_of_data['weather'][0]['icon'],
        }

    else:
        data = {}

    return render(request, "index.html", data)