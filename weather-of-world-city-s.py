import requests
import json
import pymorphy2

print('Пожалуйста, введите город, в котором желаете узнать погодные условия')

morph = pymorphy2.MorphAnalyzer()
city = str(input())
morph.parse(city)

url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)

temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
wind_speed = (weather_data['wind']['speed'])
humidity = (weather_data['main']['humidity'])

print('Сейчас в', city , str(temperature), 'градусов.', end='')
print('Ощущается как', str(temperature_feels), 'градусов. ')
print('Скорость ветра', str(wind_speed), 'м/с. ', end='')
print('Влажность воздуха', str(humidity), '%')

if wind_speed <= 5:
    print('Штиль. ',end='')
elif wind_speed <= 10:
        print('Ветренно. ',end='')
elif wind_speed <= 20:
            print('Сильные порывы ветра. ',end='')

if humidity <= 35:
    print('Ясно, небольшая облачность.')
elif humidity <=65:
        print('Пасмурно, возможны осадки.')
elif humidity <=100:
            print('Дождь.')
