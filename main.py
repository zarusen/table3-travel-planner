import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'imperial'  # Use 'metric' for Celsius, 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        
        print(f"Location: {location}")
        print(f"Temperature: {main['temp']}°F")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather_desc}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print(f"Error: {response.status_code}, unable to retrieve weather data")

if __name__ == "__main__":
    api_key = "6780e6a80eefe5dc6aca5dc07a8d416b"
    location = input("Enter the location: ")
    get_weather(api_key, location)

