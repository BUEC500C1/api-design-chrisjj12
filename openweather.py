import requests
import csv

api_key = 'd03a56cf2821428e5ad66c8317e604d1'
                
def airport_weather(airportname):
    
        with open ('airports.csv') as airports:
            try:
                listofairports = csv.DictReader(airports)

                for row in listofairports:
                    if row['name'] == airportname:
                        long = row['longitude_deg']
                        lat = row['latitude_deg']
                        url = "http://api.openweathermap.org/data/2.5/weather?" + "lat=" + lat + "&lon=" + long + "&appid=" + api_key
                        data = requests.get(url).json()

                        weather_stats= []

                        weather_stats.append("Weather: " + data['weather'][0]['description'])
                        weather_stats.append("Temperature: " + data['main']['temp'])
                        weather_stats.append("Wind speed: " +  data['wind']['speed'])
                        weather_stats.append("Humidity: " +  data['main']['humidity'])
                        weather_stats.append("Clouds: " +  data['clouds']['all'])
                        weather_stats.append("Long: " +  data['coord']['lon'] +  "Lat: " + data['coord']['lat'])
                        weather_stats.append("Humidity: " +  data['main']['humidity'])

                        return weather_stats
            except:
                print("Error")
                return []
