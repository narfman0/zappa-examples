import requests


URL = 'http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1'


def weather():
    temp = requests.get(URL).json()['main']['temp']
    return 'Temp: {}'.format(temp)
