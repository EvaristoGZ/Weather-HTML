# -*- coding: utf-8 -*-
import json
import requests
from jinja2 import Template
import webbrowser
print "Aplicación base con salida HTML || OpenWeatherMap"
print ""

def cardinal(grados):
	if (grados >= 337.5 and grados <= 360) or (grados >= 0 and grado <= 22.5):
		return 'N' 
	if grados >= 22.5 and grados <= 67.5:
		return 'NE'
	if grados >= 67.5 and grados <= 112.5:
		return 'SE'
	if grados >= 112.5 and grados <= 157.5:
		return 'S'
	if grados >= 157.5 and grados <= 202.5:
		return 'SO'
	if grados >= 202.5 and grados <= 245.5:
		return 'O'
	if grados >= 245.5 and grados <= 337.5:
		return 'NO'

fplantilla = open('plantilla.html','r')
plantilla = fplantilla
fresultado = open('resultado.html','w')

codigo = ''
for linea in fplantilla:
	codigo += linea
fplantilla = Template(codigo)
fplantilla = fplantilla.render(provincia="Lorem")

resultado = fresultado.write(fplantilla)
print fplantilla

# prov = ['Almería', 'Cádiz', 'Córdoba', 'Granada', 'Huelva', 'Jaén', 'Málaga', 'Sevilla']
# for elemento in prov:
# 	print elemento
# 	datos = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % elemento})
# 	valores = json.loads(datos.text) # Carga los datos en un diccionario json #
# 	temp_max = valores['main']['temp_max']
# 	temp_max = round(temp_max - 273,1)
# 	temp_min = valores['main']['temp_min']
# 	temp_min = round(temp_min - 273,1)
# 	velocidad = valores['wind']['speed']
# 	direccion = valores['wind']['deg']

# print datos.text

webbrowser.open("resultado.html")