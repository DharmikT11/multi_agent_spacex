import requests
import os

class WeatherAgent:
    def get_weather(self, launch_data):
        print("[WeatherAgent] Fetching weather at launch site...")
        lat = launch_data['lat']
        lon = launch_data['lon']
        key = os.getenv("OPENWEATHER_API_KEY")

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric"
        res = requests.get(url)
        weather = res.json()

        description = weather['weather'][0]['description']
        wind_speed = weather['wind']['speed']
        temp = weather['main']['temp']

        print(f"  -> Weather: {description}, Temp: {temp}°C, Wind: {wind_speed} m/s")
        return {
            "description": description,
            "temp": temp,
            "wind_speed": wind_speed
        }
