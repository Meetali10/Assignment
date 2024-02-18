import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # Use "imperial" for Fahrenheit
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

if __name__ == "__main__":
    api_key = "c8ac599d5515a8f1e3c02b1f3aa66a77"  # Replace with your OpenWeatherMap API key
    city = input("Enter a city: ")
    
    weather_info = get_weather(api_key, city)
    
    if weather_info:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_info['main']['temp']}°C")
        print(f"Description: {weather_info['weather'][0]['description']}")
        print(f"Humidity: {weather_info['main']['humidity']}%")
    else:
        print(f"Failed to retrieve weather information for {city}. Please check your input.")
