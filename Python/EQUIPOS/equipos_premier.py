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


ulrs=['https://www.resultados-futbol.com/Liverpool', 'https://www.resultados-futbol.com/Manchester-City-Fc',
'https://www.resultados-futbol.com/Leicester-City-Fc', 'https://www.resultados-futbol.com/Chelsea-Fc',
'https://www.resultados-futbol.com/Manchester-United-Fc','https://www.resultados-futbol.com/Wolverhampton',
'https://www.resultados-futbol.com/Sheffield-United','https://www.resultados-futbol.com/Tottenham-Hotspur-Fc',
'https://www.resultados-futbol.com/Arsenal','https://www.resultados-futbol.com/Burnley-Fc',
'https://www.resultados-futbol.com/Crystal-Palace-Fc','https://www.resultados-futbol.com/Everton-Fc',
'https://www.resultados-futbol.com/Newcastle-United-Fc','https://www.resultados-futbol.com/Southampton-Fc',
'https://www.resultados-futbol.com/Brighton-Amp-Hov','https://www.resultados-futbol.com/West-Ham-United',
'https://www.resultados-futbol.com/Watford-Fc','https://www.resultados-futbol.com/Afc-Bournemouth',
'https://www.resultados-futbol.com/Aston-Villa-Fc','https://www.resultados-futbol.com/Norwich-City-Fc']


equipos=['Liverpool','Man. City','Leicester','Chelsea','Man. Utd','Wolves','Sheffield United','Tottenham',
'Arsenal','Burnley','Crystal Palace','Everton','Newcastle','Southampton','Brighton Hove A.','West Ham','Watford','AFC Bournemouth',
'Aston Villa','Norwich City']


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
	
	


ulrs=['https://www.resultados-futbol.com/Liverpool', 'https://www.resultados-futbol.com/Manchester-City-Fc',
'https://www.resultados-futbol.com/Leicester-City-Fc', 'https://www.resultados-futbol.com/Chelsea-Fc',
'https://www.resultados-futbol.com/Manchester-United-Fc','https://www.resultados-futbol.com/Wolverhampton',
'https://www.resultados-futbol.com/Cardiff-City-Fc','https://www.resultados-futbol.com/Tottenham-Hotspur-Fc',
'https://www.resultados-futbol.com/Arsenal','https://www.resultados-futbol.com/Burnley-Fc',
'https://www.resultados-futbol.com/Crystal-Palace-Fc','https://www.resultados-futbol.com/Everton-Fc',
'https://www.resultados-futbol.com/Newcastle-United-Fc','https://www.resultados-futbol.com/Southampton-Fc',
'https://www.resultados-futbol.com/Brighton-Amp-Hov','https://www.resultados-futbol.com/West-Ham-United',
'https://www.resultados-futbol.com/Watford-Fc','https://www.resultados-futbol.com/Afc-Bournemouth',
'https://www.resultados-futbol.com/Fulham','https://www.resultados-futbol.com/Huddersfield-Town-Fc']


equipos=['Liverpool','Man. City','Leicester','Chelsea','Man. Utd','Wolves','Cardiff City','Tottenham',
'Arsenal','Burnley','Crystal Palace','Everton','Newcastle','Southampton','Brighton Hove A.','West Ham','Watford','AFC Bournemouth',
'Fulham','Huddersfield']
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
	
	

	
ulrs=['https://www.resultados-futbol.com/Liverpool', 'https://www.resultados-futbol.com/Manchester-City-Fc',
'https://www.resultados-futbol.com/Leicester-City-Fc', 'https://www.resultados-futbol.com/Chelsea-Fc',
'https://www.resultados-futbol.com/Manchester-United-Fc','https://www.resultados-futbol.com/Swansea-City-Afc',
'https://www.resultados-futbol.com/Stoke-City','https://www.resultados-futbol.com/Tottenham-Hotspur-Fc',
'https://www.resultados-futbol.com/Arsenal','https://www.resultados-futbol.com/Burnley-Fc',
'https://www.resultados-futbol.com/Crystal-Palace-Fc','https://www.resultados-futbol.com/Everton-Fc',
'https://www.resultados-futbol.com/Newcastle-United-Fc','https://www.resultados-futbol.com/Southampton-Fc',
'https://www.resultados-futbol.com/Brighton-Amp-Hov','https://www.resultados-futbol.com/West-Ham-United',
'https://www.resultados-futbol.com/Watford-Fc','https://www.resultados-futbol.com/Afc-Bournemouth',
'https://www.resultados-futbol.com/West-Bromwich','https://www.resultados-futbol.com/Huddersfield-Town-Fc']


equipos=['Liverpool','Man. City','Leicester','Chelsea','Man. Utd','Swansea City','Stoke City','Tottenham',
'Arsenal','Burnley','Crystal Palace','Everton','Newcastle','Southampton','Brighton Hove A.','West Ham','Watford','AFC Bournemouth',
'West Bromwich A.','Huddersfield']

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
	
	


ulrs=['https://www.resultados-futbol.com/Liverpool', 'https://www.resultados-futbol.com/Manchester-City-Fc',
'https://www.resultados-futbol.com/Leicester-City-Fc', 'https://www.resultados-futbol.com/Chelsea-Fc',
'https://www.resultados-futbol.com/Manchester-United-Fc','https://www.resultados-futbol.com/Swansea-City-Afc',
'https://www.resultados-futbol.com/Stoke-City','https://www.resultados-futbol.com/Tottenham-Hotspur-Fc',
'https://www.resultados-futbol.com/Arsenal','https://www.resultados-futbol.com/Burnley-Fc',
'https://www.resultados-futbol.com/Crystal-Palace-Fc','https://www.resultados-futbol.com/Everton-Fc',
'https://www.resultados-futbol.com/Hull-City','https://www.resultados-futbol.com/Southampton-Fc',
'https://www.resultados-futbol.com/Middlesbrough-Fc','https://www.resultados-futbol.com/West-Ham-United',
'https://www.resultados-futbol.com/Watford-Fc','https://www.resultados-futbol.com/Afc-Bournemouth',
'https://www.resultados-futbol.com/West-Bromwich','https://www.resultados-futbol.com/Sunderland-Afc']


equipos=['Liverpool','Man. City','Leicester','Chelsea','Man. Utd','Swansea City','Stoke City','Tottenham',
'Arsenal','Burnley','Crystal Palace','Everton','Hull City','Southampton','Middlesbrough','West Ham','Watford','AFC Bournemouth',
'West Bromwich A.','Sunderland']


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
	
	

	
csvfile="/home/gonzalo/Escritorio/TFG/EQUIPOS/equipos_premier.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.foto,val.nombre,val.estadio,val.entrenador,val.ubicacion])




