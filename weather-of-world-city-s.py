import requests
import json
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

print('Пожалуйста, введите город, в котором желаете узнать погодные условия')

city = str(input())
morph_city_name = morph.parse(city)[0]
sity = morph_city_name.inflect({'loct'}).word.capitalize()

url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)

temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
wind_speed = (weather_data['wind']['speed'])
humidity = (weather_data['main']['humidity'])
status_of_weather = (weather_data['weather'][0]['description'])          #Спросить позже у Котика



print('Сейчас в', sity , str(temperature), 'градусов. ', end='')
print('Ощущается как', str(temperature_feels), 'градусов. ')
print('Скорость ветра', str(wind_speed), 'м/с. ', end='')
print('Влажность воздуха', str(humidity), '%')
print(str(status_of_weather).capitalize())

if wind_speed <= 1:
    print('Штиль. ',end='')
elif wind_speed <= 10:
    print('Ветренно. ',end='')
elif wind_speed <= 20:
    print('Сильные порывы ветра. ',end='')
