import requests
Key = '20e782bf2131b3ae1381f0780e79eb7d'
def showweather(city,country):
    global filtered_list
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'.format(city,country,Key)
    
    try:
        r = requests.get(url)
        data = r.json()
        filtered_list = {
            "name" : data["name"],
            "country" : data["sys"]["country"],
            "image" : data["weather"][0]["icon"],
            "temp" : data["main"]["temp"],
            "desc" : data["weather"][0]["description"]
            
        }
    
    except KeyError:
       print('wrong values entered')
    
    else:
        return filtered_list
        
    
