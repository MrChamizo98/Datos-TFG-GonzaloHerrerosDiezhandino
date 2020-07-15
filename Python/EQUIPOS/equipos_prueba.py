#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import csv
import re
from bs4 import BeautifulSoup


class Equipo:
	temporada=""
	foto=""
	nombre=""
	estadio=""
	entrenador=""
	ubicacion=""


ulrs=['https://www.resultados-futbol.com/Real-Madrid']

equipos=['Real Madrid']

lista=[]

j=Equipo()
j.temporada="equipos_temporada"
j.foto="equipos_escudo"
j.nombre="equipos_name"
j.estadio="equipos_estadio"
j.entrenador="equipos_entrenador"
j.ubicacion="equipos_ubicacion"
lista.append(j)

temporada="Temporada2020"
itera=0
for URL in ulrs:
	p=''
	page = requests.get(URL+p)

	soup=BeautifulSoup(page.content,'html.parser')

	escudo=soup.find('div',id='previewArea')
	escudo=escudo.find('img').attrs['src']
	datos=soup.find('div',id='titlehc')
	entrenador=datos.find_all('p')
	entrenador=entrenador[0].find('span')
	estadio=soup.find('div',class_='contentitem bi-stadium')
	estadio=estadio.find_all('li')
	estadio=estadio[0].find_all('span')
	estadio=estadio[1]
	ubicacion=soup.find('div',class_='text')
	ubicacion=ubicacion.find_all('ul')
	ubicacion=ubicacion[0].find_all('li')
	nombre=ubicacion[0].find_all('span')
	nombre=nombre[1]
	ubicacion=ubicacion[4].find_all('span')
	ubicacion=ubicacion[1]

	j=Equipo()
	j.temporada=temporada
	j.foto=escudo
	j.nombre=nombre.text.encode('utf-8').strip()
	j.estadio=estadio.text.encode('utf-8').strip()
	j.entrenador=entrenador.text.encode('utf-8').strip()
	j.ubicacion=ubicacion.text.encode('utf-8').strip()
	
	lista.append(j)
	
csvfile="/home/gonzalo/Escritorio/TFG/EQUIPOS/equipos_españa.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.foto,val.nombre,val.estadio,val.entrenador,val.ubicacion])




