import requests
import csv

api_key = 'c3ac39f20eed9f70d7bd7df5aba9850d'
                
def airport_weather(airportname):
    
        with open ('airports.csv') as airports:
            weather_stats = []
            try:
                listofairports = csv.DictReader(airports)

                for row in listofairports:
    
                    if row['name'] == airportname:
                        lon = row['longitude_deg']
                        lat = row['latitude_deg']
                        url = "http://api.openweathermap.org/data/2.5/weather?" + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key
                        data = requests.get(url).json()

                        weather_stats.append("Weather: " + str(data['weather'][0]['description']))
                        weather_stats.append("Temperature: " + str(data['main']['temp']))
                        weather_stats.append("Wind speed: " +  str(data['wind']['speed']))
                        weather_stats.append("Humidity: " +  str(data['main']['humidity']))
                        weather_stats.append("Clouds: " +  str(data['clouds']['all']))
                        weather_stats.append("Long: " +  str(data['coord']['lon']) +  "Lat: " + str(data['coord']['lat']))
                        
                return weather_stats
            except:
                print("Error")
                return weather_stats

