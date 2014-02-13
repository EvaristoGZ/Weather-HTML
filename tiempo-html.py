# -*- coding: utf-8 -*-
import json
import requests
from jinja2 import Template
import webbrowser
print "Aplicación base con salida HTML || OpenWeatherMap"
print ""

prov = ['Almería', 'Cádiz', 'Córdoba', 'Granada', 'Huelva', 'Jaén', 'Málaga', 'Sevilla']
for elemento in prov:
	print elemento
	datos = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % elemento})
	valores = json.loads(datos.text) # Carga los datos en un diccionario json #
	temp_max = valores['main']['temp_max']
	temp_max = round(temp_max - 273,1)
	temp_min = valores['main']['temp_min']
	temp_min = round(temp_min - 273,1)
	velocidad = valores['wind']['speed']
	direccion = valores['wind']['deg']

print datos.text

webbrowser.open("tiempo.html")