# -*- coding: utf-8 -*-
import json
import requests
print "Aplicación base || OpenWeatherMap"
print ""

fhtml = open('tiempo.html','w')

fhtml.write('''<!DOCTYPE html>
<html>
<head>
<title>El tiempo de las provincias andaluzas</title>
</head>''')

prov = ['Almería', 'Cádiz', 'Córdoba', 'Granada', 'Huelva', 'Jaén', 'Málaga', 'Sevilla']
for elemento in prov:
	print elemento
	datos = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % elemento})
	valores = json.loads(datos.text) # Carga los datos en un diccionario json #
	temperatura = valores['main']['temp']
	temperatura = round(temperatura - 273,1)
	temp_max = valores['main']['temp_max']
	temp_max = round(temp_max,1)
	tem_min = valores['main']['temp_min']
	temp_max = round(temp_min,1)
	viento = valores['wind']['speed']

print datos.text

fhtml.write('''
</body>
</html>''')
fhtml.close()
webbrowser.open("tiempo.html")