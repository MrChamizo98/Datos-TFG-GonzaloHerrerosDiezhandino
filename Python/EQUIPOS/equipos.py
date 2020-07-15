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


ulrs=['https://www.resultados-futbol.com/Real-Madrid', 'https://www.resultados-futbol.com/Barcelona',
'https://www.resultados-futbol.com/Getafe', 'https://www.resultados-futbol.com/Atletico-Madrid',
'https://www.resultados-futbol.com/Sevilla','https://www.resultados-futbol.com/Real-Sociedad',
'https://www.resultados-futbol.com/Valencia-Cf','https://www.resultados-futbol.com/Villarreal',
'https://www.resultados-futbol.com/Athletic-Bilbao','https://www.resultados-futbol.com/Granada',
'https://www.resultados-futbol.com/Levante','https://www.resultados-futbol.com/Osasuna',
'https://www.resultados-futbol.com/Betis','https://www.resultados-futbol.com/Alaves',
'https://www.resultados-futbol.com/Valladolid','https://www.resultados-futbol.com/Eibar',
'https://www.resultados-futbol.com/Celta','https://www.resultados-futbol.com/Mallorca',
'https://www.resultados-futbol.com/Leganes','https://www.resultados-futbol.com/Espanyol']

equipos=['Real Madrid','Barcelona','Getafe','Atlético Madrid','Sevilla','Real Sociedad','Valencia','Villarreal',
'Athletic Bilbao','Granada','Levante','Osasuna','Real Betis','Alavés','Real Valladolid','Eibar','Celta de Vigo','Mallorca',
'Leganés','Espanyol']

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
	ubicacion=ubicacion[4].find_all('span')
	ubicacion=ubicacion[1]

	j=Equipo()
	j.temporada=temporada
	j.foto=escudo
	j.nombre=equipos[itera]
	j.estadio=estadio.text.encode('utf-8').strip()
	j.entrenador=entrenador.text.encode('utf-8').strip()
	j.ubicacion=ubicacion.text.encode('utf-8').strip()
	
	lista.append(j)

	itera=itera+1
	


ulrs=['https://www.resultados-futbol.com/Real-Madrid', 'https://www.resultados-futbol.com/Barcelona',
'https://www.resultados-futbol.com/Getafe', 'https://www.resultados-futbol.com/Atletico-Madrid',
'https://www.resultados-futbol.com/Sevilla','https://www.resultados-futbol.com/Real-Sociedad',
'https://www.resultados-futbol.com/Valencia-Cf','https://www.resultados-futbol.com/Villarreal',
'https://www.resultados-futbol.com/Athletic-Bilbao','https://www.resultados-futbol.com/Huesca',
'https://www.resultados-futbol.com/Levante','https://www.resultados-futbol.com/Rayo-Vallecano',
'https://www.resultados-futbol.com/Betis','https://www.resultados-futbol.com/Alaves',
'https://www.resultados-futbol.com/Valladolid','https://www.resultados-futbol.com/Eibar',
'https://www.resultados-futbol.com/Celta','https://www.resultados-futbol.com/Girona-Fc',
'https://www.resultados-futbol.com/Leganes','https://www.resultados-futbol.com/Espanyol']


equipos=['Real Madrid','Barcelona','Getafe','Atlético Madrid','Sevilla','Real Sociedad','Valencia','Villarreal',
'Athletic Bilbao','Huesca','Levante','Rayo Vallecano','Real Betis','Alavés','Real Valladolid','Eibar','Celta de Vigo','Girona',
'Leganés','Espanyol']

temporada="Temporada2019"
itera=0
for URL in ulrs:
	
	#URL='https://www.resultados-futbol.com/Real-Madrid'
	#temporada 2018/2019
	p='/2019'
	#temporada 2017/2018
	#p='/2018'
	#temporada 2016/2017
	#p='/2017'
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
	ubicacion=ubicacion[4].find_all('span')
	ubicacion=ubicacion[1]

	j=Equipo()
	j.temporada=temporada
	j.foto=escudo
	j.nombre=equipos[itera]
	j.estadio=estadio.text.encode('utf-8').strip()
	j.entrenador=entrenador.text.encode('utf-8').strip()
	j.ubicacion=ubicacion.text.encode('utf-8').strip()
	
	lista.append(j)
	
	itera=itera+1
	

	
ulrs=['https://www.resultados-futbol.com/Real-Madrid', 'https://www.resultados-futbol.com/Barcelona',
'https://www.resultados-futbol.com/Getafe', 'https://www.resultados-futbol.com/Atletico-Madrid',
'https://www.resultados-futbol.com/Sevilla','https://www.resultados-futbol.com/Real-Sociedad',
'https://www.resultados-futbol.com/Valencia-Cf','https://www.resultados-futbol.com/Villarreal',
'https://www.resultados-futbol.com/Athletic-Bilbao','https://www.resultados-futbol.com/Malaga',
'https://www.resultados-futbol.com/Levante','https://www.resultados-futbol.com/Deportivo',
'https://www.resultados-futbol.com/Betis','https://www.resultados-futbol.com/Alaves',
'https://www.resultados-futbol.com/Ud-Palmas','https://www.resultados-futbol.com/Eibar',
'https://www.resultados-futbol.com/Celta','https://www.resultados-futbol.com/Girona-Fc',
'https://www.resultados-futbol.com/Leganes','https://www.resultados-futbol.com/Espanyol']

equipos=['Real Madrid','Barcelona','Getafe','Atlético Madrid','Sevilla','Real Sociedad','Valencia','Villarreal',
'Athletic Bilbao','Málaga','Levante','Deportivo','Real Betis','Alavés','Las Palmas','Eibar','Celta de Vigo','Girona',
'Leganés','Espanyol']

temporada="Temporada2018"
itera=0
for URL in ulrs:
	#temporada 2017/2018
	p='/2018'
	#temporada 2016/2017
	#p='/2017'
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
	ubicacion=ubicacion[4].find_all('span')
	ubicacion=ubicacion[1]

	j=Equipo()
	j.temporada=temporada
	j.foto=escudo
	j.nombre=equipos[itera]
	j.estadio=estadio.text.encode('utf-8').strip()
	j.entrenador=entrenador.text.encode('utf-8').strip()
	j.ubicacion=ubicacion.text.encode('utf-8').strip()
	
	lista.append(j)
	itera=itera+1
	


ulrs=['https://www.resultados-futbol.com/Real-Madrid', 'https://www.resultados-futbol.com/Barcelona',
'https://www.resultados-futbol.com/Granada', 'https://www.resultados-futbol.com/Atletico-Madrid',
'https://www.resultados-futbol.com/Sevilla','https://www.resultados-futbol.com/Real-Sociedad',
'https://www.resultados-futbol.com/Valencia-Cf','https://www.resultados-futbol.com/Villarreal',
'https://www.resultados-futbol.com/Athletic-Bilbao','https://www.resultados-futbol.com/Malaga',
'https://www.resultados-futbol.com/Sporting-Gijon','https://www.resultados-futbol.com/Deportivo',
'https://www.resultados-futbol.com/Betis','https://www.resultados-futbol.com/Alaves',
'https://www.resultados-futbol.com/Ud-Palmas','https://www.resultados-futbol.com/Eibar',
'https://www.resultados-futbol.com/Celta','https://www.resultados-futbol.com/Osasuna',
'https://www.resultados-futbol.com/Leganes','https://www.resultados-futbol.com/Espanyol']

equipos=['Real Madrid','Barcelona','Granada','Atlético Madrid','Sevilla','Real Sociedad','Valencia','Villarreal',
'Athletic Bilbao','Málaga','Real Sporting','Deportivo','Real Betis','Alavés','Las Palmas','Eibar','Celta de Vigo','Osasuna',
'Leganés','Espanyol']

temporada="Temporada2017"
itera=0
for URL in ulrs:
	#temporada 2016/2017
	p='/2017'
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
	ubicacion=ubicacion[4].find_all('span')
	ubicacion=ubicacion[1]

	j=Equipo()
	j.temporada=temporada
	j.foto=escudo
	j.nombre=equipos[itera]
	j.estadio=estadio.text.encode('utf-8').strip()
	j.entrenador=entrenador.text.encode('utf-8').strip()
	j.ubicacion=ubicacion.text.encode('utf-8').strip()
	
	lista.append(j)

	itera=itera+1
	
	

	
csvfile="/home/gonzalo/Escritorio/TFG/EQUIPOS/equipos_españa.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.foto,val.nombre,val.estadio,val.entrenador,val.ubicacion])




