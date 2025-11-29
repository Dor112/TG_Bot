import requests
import datetime
import math


async def get_wheather():
    date = datetime.datetime.today()
    formated_date = date.strftime("%d.%m.%Y %H:%M")
    res = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Moscow,ru&APPID=08f1d6a9d1833292f9d102f34ae01b3b')
    data = res.json()
    date_out = 'Сейчас: ' +  str(formated_date)
    state = "Состояние: " +  str(data['weather'][0]['description'])
    temp = "Температура: " + str(math.floor(data['main']['temp']-273.50))
    min_temp = "Минимальная температура: " + str(math.floor(data['main']['temp_min']-273.50))
    max_temp = "Максимальная температура: " + str(math.floor(data['main']['temp_max']-273.50))
    str_output = date_out +"       "+ state +"          "+ temp +"          "+  min_temp +"          "+ max_temp
    return str_output
