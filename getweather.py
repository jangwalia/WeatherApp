from flask import render_template
import requests

Key = '20e782bf2131b3ae1381f0780e79eb7d'
def showweather(city,country):
    
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'.format(city,country,Key)
    
    try:
        r = requests.get(url)
        data = r.json()
        icon = data["weather"][0]["icon"]
        if icon:
            filtered_list = {
                "name" : data["name"],
                "country" : data["sys"]["country"],
                "image" : icon,
                "temp" : data["main"]["temp"],
                "desc" : data["weather"][0]["description"]
                    
                }
            print(filtered_list)
            return filtered_list
        
        else:
            print('city not found')
    except:
        warning = 'Please enter correct value'
        return render_template('error.html',message = warning)
        
    """ try:    
        filtered_list = {
            "name" : data["name"],
            "country" : data["sys"]["country"],
            "image" : data["weather"][0]["icon"],
            "temp" : data["main"]["temp"],
            "desc" : data["weather"][0]["description"]
            
        }
        print(filtered_list)
        return filtered_list
    
    except:
       warning = 'Please enter correct value'
       return render_template('error.html',message = warning)
     """
    
        
        
    
