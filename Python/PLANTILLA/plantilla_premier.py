#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import csv
import re
from bs4 import BeautifulSoup


class Jugador:
	temporada=""
	foto=""
	pais=""
	equipo=""
	nombre=""
	edad=""
	goles=""
	rojas=""
	amarillas=""
	dorsal=""
	altura=""
	peso=""
	posicion=""


ulrs=['https://www.resultados-futbol.com/plantilla/Liverpool', 'https://www.resultados-futbol.com/plantilla/Manchester-City-Fc',
'https://www.resultados-futbol.com/plantilla/Leicester-City-Fc', 'https://www.resultados-futbol.com/plantilla/Chelsea-Fc',
'https://www.resultados-futbol.com/plantilla/Manchester-United-Fc','https://www.resultados-futbol.com/plantilla/Wolverhampton',
'https://www.resultados-futbol.com/plantilla/Sheffield-United','https://www.resultados-futbol.com/plantilla/Tottenham-Hotspur-Fc',
'https://www.resultados-futbol.com/plantilla/Arsenal','https://www.resultados-futbol.com/plantilla/Burnley-Fc',
'https://www.resultados-futbol.com/plantilla/Crystal-Palace-Fc','https://www.resultados-futbol.com/plantilla/Everton-Fc',
'https://www.resultados-futbol.com/plantilla/Newcastle-United-Fc','https://www.resultados-futbol.com/plantilla/Southampton-Fc',
'https://www.resultados-futbol.com/plantilla/Brighton-Amp-Hov','https://www.resultados-futbol.com/plantilla/West-Ham-United',
'https://www.resultados-futbol.com/plantilla/Watford-Fc','https://www.resultados-futbol.com/plantilla/Afc-Bournemouth',
'https://www.resultados-futbol.com/plantilla/Aston-Villa-Fc','https://www.resultados-futbol.com/plantilla/Norwich-City-Fc']


equipos=['Liverpool','Man. City','Leicester','Chelsea','Man. Utd','Wolves','Sheffield United','Tottenham',
'Arsenal','Burnley','Crystal Palace','Everton','Newcastle','Southampton','Brighton Hove A.','West Ham','Watford','AFC Bournemouth',
'Aston Villa','Norwich City']

lista=[]

j=Jugador()
j.temporada="plantilla_temporada"
j.foto='plantilla_foto'
j.pais='plantilla_pais'
j.equipo='plantilla_equipo'
j.nombre='plantilla_name'
j.edad='plantilla_edad'
j.goles='plantilla_goles'
j.rojas='plantilla_rojas'
j.amarillas='plantilla_amarillas'
j.dorsal='plantilla_dorsal'
j.altura='plantilla_altura'
j.peso='plantilla_peso'
j.posicion='plantilla_posicion'
lista.append(j)

temporada="Temporada2020"
itera=0
for URL in ulrs:
	p=''
	#URL='https://www.resultados-futbol.com/plantilla/Real-Madrid'
	#temporada 2018/2019
	#p='/2019'
	#temporada 2017/2018
	#p='/2018'
	#temporada 2016/2017
	#p='/2017'
	page = requests.get(URL+p)

	soup=BeautifulSoup(page.content,'html.parser')

	results=soup.find(class_='sdata_table')
	if results is None:
		continue
	tabla=results.find('tbody')
	if tabla is None:
		continue
	filas=tabla.find_all('tr')
	if filas is None:
		continue
	posicion=""

	for i in filas:
		s=i.text.encode('utf-8').strip()
		if s in ('Portero','Defensa','Centrocampista','Delantero'):
			posicion=i.text.encode('utf-8').strip()
			continue
		numero=i.find(class_='num')
		foto=i.find(class_='sdata_player_img')
		foto=foto.find('img').attrs['src']
		nombre=i.find(class_='sdata_player_name')
		edad=i.find(class_='birthdate')
		pais=i.find(class_='ori')
		pais=pais.find('img').attrs['src']
		datos=i.find_all('td', class_='dat')
		altura=datos[0]
		peso=datos[1]
		goles=datos[2]
		rojas=datos[3]
		amarillas=datos[4]
		equipo=equipos[itera]

		j=Jugador()
		j.temporada=temporada
		j.foto=foto
		j.pais=pais
		j.equipo=equipo
		j.nombre=nombre.text.encode('utf-8').strip()
		j.edad=edad.text.encode('utf-8').strip()
		if goles.text.encode('utf-8').strip() is '-':
			j.goles='0'
		else:
			j.goles=goles.text.encode('utf-8').strip()
		if rojas.text.encode('utf-8').strip() is '-':
			j.rojas='0'
		else:
			j.rojas=rojas.text.encode('utf-8').strip()
		if amarillas.text.encode('utf-8').strip() is '-':
			j.amarillas='0'
		else:
			j.amarillas=amarillas.text.encode('utf-8').strip()
		j.dorsal=numero.text.encode('utf-8').strip()
		j.altura=altura.text.encode('utf-8').strip()
		j.peso=peso.text.encode('utf-8').strip()
		j.posicion=posicion

		lista.append(j)
	itera=itera+1;

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_premier_2019_2020.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])


ulrs=['https://www.resultados-futbol.com/plantilla/Liverpool', 'https://www.resultados-futbol.com/plantilla/Manchester-City-Fc',
'https://www.resultados-futbol.com/plantilla/Leicester-City-Fc', 'https://www.resultados-futbol.com/plantilla/Chelsea-Fc',
'https://www.resultados-futbol.com/plantilla/Manchester-United-Fc','https://www.resultados-futbol.com/plantilla/Wolverhampton',
'https://www.resultados-futbol.com/plantilla/Cardiff-City-Fc','https://www.resultados-futbol.com/plantilla/Tottenham-Hotspur-Fc',
'https://www.resultados-futbol.com/plantilla/Arsenal','https://www.resultados-futbol.com/plantilla/Burnley-Fc',
'https://www.resultados-futbol.com/plantilla/Crystal-Palace-Fc','https://www.resultados-futbol.com/plantilla/Everton-Fc',
'https://www.resultados-futbol.com/plantilla/Newcastle-United-Fc','https://www.resultados-futbol.com/plantilla/Southampton-Fc',
'https://www.resultados-futbol.com/plantilla/Brighton-Amp-Hov','https://www.resultados-futbol.com/plantilla/West-Ham-United',
'https://www.resultados-futbol.com/plantilla/Watford-Fc','https://www.resultados-futbol.com/plantilla/Afc-Bournemouth',
'https://www.resultados-futbol.com/plantilla/Fulham','https://www.resultados-futbol.com/plantilla/Huddersfield-Town-Fc']


equipos=['Liverpool','Man. City','Leicester','Chelsea','Man. Utd','Wolves','Cardiff City','Tottenham',
'Arsenal','Burnley','Crystal Palace','Everton','Newcastle','Southampton','Brighton Hove A.','West Ham','Watford','AFC Bournemouth',
'Fulham','Huddersfield']

lista=[]

j=Jugador()
j.temporada="plantilla_temporada"
j.foto='plantilla_foto'
j.pais='plantilla_pais'
j.equipo='plantilla_equipo'
j.nombre='plantilla_name'
j.edad='plantilla_edad'
j.goles='plantilla_goles'
j.rojas='plantilla_rojas'
j.amarillas='plantilla_amarillas'
j.dorsal='plantilla_dorsal'
j.altura='plantilla_altura'
j.peso='plantilla_peso'
j.posicion='plantilla_posicion'
lista.append(j)

temporada="Temporada2019"
itera=0
for URL in ulrs:
	p='/2019'
	#temporada 2017/2018
	#p='/2018'
	#temporada 2016/2017
	#p='/2017'
	page = requests.get(URL+p)

	soup=BeautifulSoup(page.content,'html.parser')

	results=soup.find(class_='sdata_table')
	if results is None:
		continue
	tabla=results.find('tbody')
	if tabla is None:
		continue
	filas=tabla.find_all('tr')
	if filas is None:
		continue
	posicion=""

	for i in filas:
		s=i.text.encode('utf-8').strip()
		if s in ('Portero','Defensa','Centrocampista','Delantero'):
			posicion=i.text.encode('utf-8').strip()
			continue
		numero=i.find(class_='num')
		foto=i.find(class_='sdata_player_img')
		foto=foto.find('img').attrs['src']
		nombre=i.find(class_='sdata_player_name')
		edad=i.find(class_='birthdate')
		pais=i.find(class_='ori')
		pais=pais.find('img').attrs['src']
		datos=i.find_all('td', class_='dat')
		altura=datos[0]
		peso=datos[1]
		goles=datos[2]
		rojas=datos[3]
		amarillas=datos[4]
		equipo=equipos[itera]

		j=Jugador()
		j.temporada=temporada
		j.foto=foto
		j.pais=pais
		j.equipo=equipo
		j.nombre=nombre.text.encode('utf-8').strip()
		j.edad=edad.text.encode('utf-8').strip()
		if goles.text.encode('utf-8').strip() is '-':
			j.goles='0'
		else:
			j.goles=goles.text.encode('utf-8').strip()
		if rojas.text.encode('utf-8').strip() is '-':
			j.rojas='0'
		else:
			j.rojas=rojas.text.encode('utf-8').strip()
		if amarillas.text.encode('utf-8').strip() is '-':
			j.amarillas='0'
		else:
			j.amarillas=amarillas.text.encode('utf-8').strip()
		j.dorsal=numero.text.encode('utf-8').strip()
		j.altura=altura.text.encode('utf-8').strip()
		j.peso=peso.text.encode('utf-8').strip()
		j.posicion=posicion

		lista.append(j)
	itera=itera+1;

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_premier_2018_2019.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])


ulrs=['https://www.resultados-futbol.com/plantilla/Liverpool', 'https://www.resultados-futbol.com/plantilla/Manchester-City-Fc',
'https://www.resultados-futbol.com/plantilla/Leicester-City-Fc', 'https://www.resultados-futbol.com/plantilla/Chelsea-Fc',
'https://www.resultados-futbol.com/plantilla/Manchester-United-Fc','https://www.resultados-futbol.com/plantilla/Swansea-City-Afc',
'https://www.resultados-futbol.com/plantilla/Stoke-City','https://www.resultados-futbol.com/plantilla/Tottenham-Hotspur-Fc',
'https://www.resultados-futbol.com/plantilla/Arsenal','https://www.resultados-futbol.com/plantilla/Burnley-Fc',
'https://www.resultados-futbol.com/plantilla/Crystal-Palace-Fc','https://www.resultados-futbol.com/plantilla/Everton-Fc',
'https://www.resultados-futbol.com/plantilla/Newcastle-United-Fc','https://www.resultados-futbol.com/plantilla/Southampton-Fc',
'https://www.resultados-futbol.com/plantilla/Brighton-Amp-Hov','https://www.resultados-futbol.com/plantilla/West-Ham-United',
'https://www.resultados-futbol.com/plantilla/Watford-Fc','https://www.resultados-futbol.com/plantilla/Afc-Bournemouth',
'https://www.resultados-futbol.com/plantilla/West-Bromwich','https://www.resultados-futbol.com/plantilla/Huddersfield-Town-Fc']


equipos=['Liverpool','Man. City','Leicester','Chelsea','Man. Utd','Swansea City','Stoke City','Tottenham',
'Arsenal','Burnley','Crystal Palace','Everton','Newcastle','Southampton','Brighton Hove A.','West Ham','Watford','AFC Bournemouth',
'West Bromwich A.','Huddersfield']
lista=[]

j=Jugador()
j.temporada="plantilla_temporada"
j.foto='plantilla_foto'
j.pais='plantilla_pais'
j.equipo='plantilla_equipo'
j.nombre='plantilla_name'
j.edad='plantilla_edad'
j.goles='plantilla_goles'
j.rojas='plantilla_rojas'
j.amarillas='plantilla_amarillas'
j.dorsal='plantilla_dorsal'
j.altura='plantilla_altura'
j.peso='plantilla_peso'
j.posicion='plantilla_posicion'
lista.append(j)

temporada="Temporada2018"
itera=0
for URL in ulrs:
	p='/2018'
	#temporada 2016/2017
	#p='/2017'
	page = requests.get(URL+p)

	soup=BeautifulSoup(page.content,'html.parser')

	results=soup.find(class_='sdata_table')
	if results is None:
		continue
	tabla=results.find('tbody')
	if tabla is None:
		continue
	filas=tabla.find_all('tr')
	if filas is None:
		continue
	posicion=""

	for i in filas:
		s=i.text.encode('utf-8').strip()
		if s in ('Portero','Defensa','Centrocampista','Delantero'):
			posicion=i.text.encode('utf-8').strip()
			continue
		numero=i.find(class_='num')
		foto=i.find(class_='sdata_player_img')
		foto=foto.find('img').attrs['src']
		nombre=i.find(class_='sdata_player_name')
		edad=i.find(class_='birthdate')
		pais=i.find(class_='ori')
		pais=pais.find('img').attrs['src']
		datos=i.find_all('td', class_='dat')
		altura=datos[0]
		peso=datos[1]
		goles=datos[2]
		rojas=datos[3]
		amarillas=datos[4]
		equipo=equipos[itera]

		j=Jugador()
		j.temporada=temporada
		j.foto=foto
		j.pais=pais
		j.equipo=equipo
		j.nombre=nombre.text.encode('utf-8').strip()
		j.edad=edad.text.encode('utf-8').strip()
		if goles.text.encode('utf-8').strip() is '-':
			j.goles='0'
		else:
			j.goles=goles.text.encode('utf-8').strip()
		if rojas.text.encode('utf-8').strip() is '-':
			j.rojas='0'
		else:
			j.rojas=rojas.text.encode('utf-8').strip()
		if amarillas.text.encode('utf-8').strip() is '-':
			j.amarillas='0'
		else:
			j.amarillas=amarillas.text.encode('utf-8').strip()
		j.dorsal=numero.text.encode('utf-8').strip()
		j.altura=altura.text.encode('utf-8').strip()
		j.peso=peso.text.encode('utf-8').strip()
		j.posicion=posicion

		lista.append(j)
	itera=itera+1;

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_premier_2017_2018.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])


ulrs=['https://www.resultados-futbol.com/plantilla/Liverpool', 'https://www.resultados-futbol.com/plantilla/Manchester-City-Fc',
'https://www.resultados-futbol.com/plantilla/Leicester-City-Fc', 'https://www.resultados-futbol.com/plantilla/Chelsea-Fc',
'https://www.resultados-futbol.com/plantilla/Manchester-United-Fc','https://www.resultados-futbol.com/plantilla/Swansea-City-Afc',
'https://www.resultados-futbol.com/plantilla/Stoke-City','https://www.resultados-futbol.com/plantilla/Tottenham-Hotspur-Fc',
'https://www.resultados-futbol.com/plantilla/Arsenal','https://www.resultados-futbol.com/plantilla/Burnley-Fc',
'https://www.resultados-futbol.com/plantilla/Crystal-Palace-Fc','https://www.resultados-futbol.com/plantilla/Everton-Fc',
'https://www.resultados-futbol.com/plantilla/Hull-City','https://www.resultados-futbol.com/plantilla/Southampton-Fc',
'https://www.resultados-futbol.com/plantilla/Middlesbrough-Fc','https://www.resultados-futbol.com/plantilla/West-Ham-United',
'https://www.resultados-futbol.com/plantilla/Watford-Fc','https://www.resultados-futbol.com/plantilla/Afc-Bournemouth',
'https://www.resultados-futbol.com/plantilla/West-Bromwich','https://www.resultados-futbol.com/plantilla/Sunderland-Afc']


equipos=['Liverpool','Man. City','Leicester','Chelsea','Man. Utd','Swansea City','Stoke City','Tottenham',
'Arsenal','Burnley','Crystal Palace','Everton','Hull City','Southampton','Middlesbrough','West Ham','Watford','AFC Bournemouth',
'West Bromwich A.','Sunderland']
lista=[]
j=Jugador()
j.temporada="plantilla_temporada"
j.foto='plantilla_foto'
j.pais='plantilla_pais'
j.equipo='plantilla_equipo'
j.nombre='plantilla_name'
j.edad='plantilla_edad'
j.goles='plantilla_goles'
j.rojas='plantilla_rojas'
j.amarillas='plantilla_amarillas'
j.dorsal='plantilla_dorsal'
j.altura='plantilla_altura'
j.peso='plantilla_peso'
j.posicion='plantilla_posicion'
lista.append(j)

temporada="Temporada2017"
itera=0
for URL in ulrs:
	p='/2017'
	page = requests.get(URL+p)

	soup=BeautifulSoup(page.content,'html.parser')

	results=soup.find(class_='sdata_table')
	if results is None:
		continue
	tabla=results.find('tbody')
	if tabla is None:
		continue
	filas=tabla.find_all('tr')
	if filas is None:
		continue
	posicion=""

	for i in filas:
		s=i.text.encode('utf-8').strip()
		if s in ('Portero','Defensa','Centrocampista','Delantero'):
			posicion=i.text.encode('utf-8').strip()
			continue
		numero=i.find(class_='num')
		foto=i.find(class_='sdata_player_img')
		foto=foto.find('img').attrs['src']
		nombre=i.find(class_='sdata_player_name')
		edad=i.find(class_='birthdate')
		pais=i.find(class_='ori')
		pais=pais.find('img').attrs['src']
		datos=i.find_all('td', class_='dat')
		altura=datos[0]
		peso=datos[1]
		goles=datos[2]
		rojas=datos[3]
		amarillas=datos[4]
		equipo=equipos[itera]

		j=Jugador()
		j.temporada=temporada
		j.foto=foto
		j.pais=pais
		j.equipo=equipo
		j.nombre=nombre.text.encode('utf-8').strip()
		j.edad=edad.text.encode('utf-8').strip()
		if goles.text.encode('utf-8').strip() is '-':
			j.goles='0'
		else:
			j.goles=goles.text.encode('utf-8').strip()
		if rojas.text.encode('utf-8').strip() is '-':
			j.rojas='0'
		else:
			j.rojas=rojas.text.encode('utf-8').strip()
		if amarillas.text.encode('utf-8').strip() is '-':
			j.amarillas='0'
		else:
			j.amarillas=amarillas.text.encode('utf-8').strip()
		j.dorsal=numero.text.encode('utf-8').strip()
		j.altura=altura.text.encode('utf-8').strip()
		j.peso=peso.text.encode('utf-8').strip()
		j.posicion=posicion

		lista.append(j)
	itera=itera+1;

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_premier_2016_2017.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])

