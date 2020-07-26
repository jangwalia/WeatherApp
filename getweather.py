import requests

def showweather():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=surrey,CA&units=metric&appid=20e782bf2131b3ae1381f0780e79eb7d'
    r = requests.get(url)
    data = r.json()
    return(data)
