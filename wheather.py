import requests
import datetime
import math

async def get_wheather():
    date = datetime.datetime.today()
    formatted_date = date.strftime("%d.%m.%Y %H:%M")

    res = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "q": "Moscow,ru",
            "appid": "08f1d6a9d1833292f9d102f34ae01b3b",
            "lang": "ru"
        }
    )
    data = res.json()

    temp = math.floor(data["main"]["temp"] - 273.15)
    temp_min = math.floor(data["main"]["temp_min"] - 273.15)
    temp_max = math.floor(data["main"]["temp_max"] - 273.15)
    state = data["weather"][0]["description"]

    weather_text = (
        f"📅 Сейчас: {formatted_date}\n"
        f"🌤 Состояние: {state}\n"
        f"🌡 Температура: {temp}°C\n"
        f"⬇️ Мин: {temp_min}°C | ⬆️ Макс: {temp_max}°C"
    )

    return weather_text