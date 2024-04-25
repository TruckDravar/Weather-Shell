import requests
import terminal_alignment


api_key = "cfe8345fd93bfd4cca0e526839712974"


# fetches weather info from api as json file
def fetch_weather(api_key, city, unit):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&limit=2&appid={api_key}&units={unit}"
    response = requests.get(url)
    data = response.json()
    return data


# checks for weather info then returns its value
def weather_info(city, unit):

    key = api_key
    weather_temperature = ""
    weather_description = ""
    max_temperature = ""
    min_temperature = ""
    feels_like = ""
    humidity = ""
    pressure = ""

    weather_data = fetch_weather(api_key, city, unit)
    try:
        if weather_data["cod"] == 200:
            weather_description = weather_data["weather"][0]["description"]
            weather_temperature = weather_data["main"]["temp"]
            max_temperature = weather_data["main"]["temp_max"]
            min_temperature = weather_data["main"]["temp_min"]
            feels_like = weather_data["main"]["feels_like"]
            humidity = weather_data["main"]["humidity"]
            pressure = weather_data["main"]["pressure"]

    except AttributeError:
        print("Invalid Input")

    return (
        weather_temperature,
        weather_description,
        max_temperature,
        min_temperature,
        feels_like,
        humidity,
        pressure,
    )


# fetches forcast
def fetch_forecast(api_key, city, unit):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={unit}"
    response = requests.get(url)
    data = response.json()
    return data


# returns forecast info
def forecast_info(city, unit):
    key = api_key
    forecast_time = ""
    forecast_temperature = ""
    forecast_description = ""
    si_unit = unit
    if si_unit == "metric":
        si_unit = "°C"
    elif si_unit == "imperial":
        si_unit = "°F"
    else:
        si_unit = "K"

    forecast_data = fetch_forecast(key, city, unit)

    forecast_list = forecast_data["list"]

    terminal_alignment.print_center(f"3-Hour Forecast for {city.capitalize()}:")
    terminal_alignment.print_center(
        "{:<20} {:<15} {:<20}".format(
            "Time", "Temperature ({})".format(si_unit), "Description"
        )
    )
    terminal_alignment.print_center("-" * 55)
    for forecast in forecast_list:
        forecast_time = forecast["dt_txt"]
        forecast_temperature = forecast["main"]["temp"]
        forecast_description = forecast["weather"][0]["description"]
        terminal_alignment.print_center(
            "{:<20} {:<15.2f} {:<20}".format(
                forecast_time, forecast_temperature, forecast_description
            )
        )

    return 0


def fetch_aqi(city):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    try:
        # Extract AQI value from the response
        aqi = data["results"][0]["measurements"][0]["value"]
        return aqi
    except (KeyError, IndexError):
        return None
