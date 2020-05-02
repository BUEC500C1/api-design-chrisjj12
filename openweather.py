import requests
import csv

api_key = 'd03a56cf2821428e5ad66c8317e604d1'
                
def airport_weather(airportname):
    
    with open ('airports.csv') as airports:
        listofairports = csv.DictReader(airports)

        for row in listofairports:
            if row['name'] == airportname:
                long = row['longitude_deg']
                lat = row['latitude_deg']
                url = "http://api.openweathermap.org/data/2.5/weather?" + "lat=" + lat + "&lon=" + long + "&appid=" + api_key
                data = requests.get(url).json()

                print("Weather: ", data['weather'][0]['description'])
                print("Temperature: ", data['main']['temp'])
                print("Wind speed: ", data['wind']['speed'])
                print("Humidity: ", data['main']['humidity'])
                print("Clouds: ", data['clouds']['all'])
                print("Long:", data['coord']['lon'], "Lat:",data['coord']['lat'])
                print("Humidity:", data['main']['humidity'])
            #else
                #print("Invalid airport, please enter a valid airport!")
