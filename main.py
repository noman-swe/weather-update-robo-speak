import requests
import json
import win32com.client as wincom

city = input("Enter the city name \n")

url = f"http://api.weatherapi.com/v1/current.json?key=349a4a7f64bf444b9cd162705230310&q={city}"
r = requests.get(url)
# print(r.text)
#  print(type(r.text)) #r.text is a string but if we want to make it as dictionary then we have to do bolow things

#making string to dictionary

#weatherData = json.loads(r.text)
#another process to use json to make dictionary
weatherData = r.json()
# print(type(weatherData)) #it is a dictionary

# check if the request was successful
if "error" in weatherData:
    print(f"Error: {weatherData['error']['message']}")
else:
    # current temp
    currentTemperature = weatherData["current"]["temp_c"]
    # print(currentTemperature)

    # country name
    country = weatherData["location"]["country"]

    # weather condition
    weatherCondition = weatherData["current"]["condition"]["text"]

    # wind per kilometer
    windPerKilo = weatherData["current"]["wind_kph"]

    # Humidity
    humidity = weatherData["current"]["humidity"]

    # cloud
    cloud = weatherData["current"]["cloud"]

    # Local time
    localTime = weatherData["location"]["localtime"]

    # weather last update date
    weatherUpdateDate = weatherData["current"]["last_updated"]

    robo = "I am Robo Weather Engineer."

    # text to voice system
    speak = wincom.Dispatch("SAPI.SpVoice")

    text = f"You are from {city}, {country}. The current weather in {city} is {currentTemperature}°C. The weather condition is {weatherCondition}, with a wind speed of {windPerKilo} km/h, humidity at {humidity}%, and cloud cover at {cloud}%. I am {robo}, reporting time is {localTime}, and the weather was last updated on {weatherUpdateDate}."

    print(text)

    # speaking print
    speak.Speak(text)