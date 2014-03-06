# -*- coding: utf-8 -*-
import json
import requests
from jinja2 import Template
import webbrowser
print "Aplicación base con salida HTML || OpenWeatherMap"
print ""

def cardinal(direccion):
	if (direccion >= 337.5 and direccion <= 360) or (direccion >= 0 and direccion <= 22.5):
		return 'N' 
	if direccion >= 22.5 and direccion <= 67.5:
		return 'NE'
	if direccion > 67.5 and direccion <= 112.5:
		return 'SE'
	if direccion > 112.5 and direccion <= 157.5:
		return 'S'
	if direccion > 157.5 and direccion <= 202.5:
		return 'SO'
	if direccion > 202.5 and direccion <= 245.5:
		return 'O'
	if direccion > 245.5 and direccion <= 292.5:
		return 'E'
	if direccion > 292.5 and direccion < 337.5:
		return 'NO'

fplantilla = open('plantilla.html','r')
plantilla = fplantilla
fresultado = open('resultado.html','w')

codigo = ''
for linea in plantilla:
	codigo += linea

alltemp_max = []
alltemp_min = []
allvelocidad = []
alldireccion = []
allpuntocardinal = []

plantilla = Template(codigo)
print fplantilla

prov = ['Almería', 'Cádiz', 'Córdoba', 'Huelva', 'Jaén', 'Málaga', 'Sevilla']
for elemento in prov:
 	print elemento
 	datos = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % elemento})
 	valores = json.loads(datos.text) # Carga los datos en un diccionario json #
 	temp_max = valores['main']['temp_max']
 	temp_max = round(temp_max - 273)
 	temp_min = valores['main']['temp_min']
 	temp_min = round(temp_min - 273)
 	velocidad = round((valores['wind']['speed']*1.609),1)
 	direccion = valores['wind']['deg']
 	puntocardinal = cardinal(direccion)
 	alltemp_max.append(temp_max)
 	alltemp_min.append(temp_min)
 	allvelocidad.append(velocidad)
 	allpuntocardinal.append(puntocardinal)
 	print temp_max
 	print temp_min
 	print velocidad
 	print puntocardinal


#webbrowser.open("resultado.html")