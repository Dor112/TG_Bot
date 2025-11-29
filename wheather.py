import requests

async def get_wheather():

    url = f'https://wttr.in/{"Moscow"}?format=%c+%C+%t+%h+%w+%p'

    response = requests.get(url)
    global output
    output = "Погода сегодня:" + response.text
    return output