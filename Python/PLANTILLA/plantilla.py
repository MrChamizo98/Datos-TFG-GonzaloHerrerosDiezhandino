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


ulrs=['https://www.resultados-futbol.com/plantilla/Real-Madrid', 'https://www.resultados-futbol.com/plantilla/Barcelona',
'https://www.resultados-futbol.com/plantilla/Getafe', 'https://www.resultados-futbol.com/plantilla/Atletico-Madrid',
'https://www.resultados-futbol.com/plantilla/Sevilla','https://www.resultados-futbol.com/plantilla/Real-Sociedad',
'https://www.resultados-futbol.com/plantilla/Valencia-Cf','https://www.resultados-futbol.com/plantilla/Villarreal',
'https://www.resultados-futbol.com/plantilla/Athletic-Bilbao','https://www.resultados-futbol.com/plantilla/Granada',
'https://www.resultados-futbol.com/plantilla/Levante','https://www.resultados-futbol.com/plantilla/Osasuna',
'https://www.resultados-futbol.com/plantilla/Betis','https://www.resultados-futbol.com/plantilla/Alaves',
'https://www.resultados-futbol.com/plantilla/Valladolid','https://www.resultados-futbol.com/plantilla/Eibar',
'https://www.resultados-futbol.com/plantilla/Celta','https://www.resultados-futbol.com/plantilla/Mallorca',
'https://www.resultados-futbol.com/plantilla/Leganes','https://www.resultados-futbol.com/plantilla/Espanyol']

equipos=['Real Madrid','Barcelona','Getafe','Atlético Madrid','Sevilla','Real Sociedad','Valencia','Villarreal',
'Athletic Bilbao','Granada','Levante','Osasuna','Real Betis','Alavés','Real Valladolid','Eibar','Celta de Vigo','Mallorca',
'Leganés','Espanyol']

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

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_españa_2019_2020.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])


ulrs=['https://www.resultados-futbol.com/plantilla/Real-Madrid', 'https://www.resultados-futbol.com/plantilla/Barcelona',
'https://www.resultados-futbol.com/plantilla/Getafe', 'https://www.resultados-futbol.com/plantilla/Atletico-Madrid',
'https://www.resultados-futbol.com/plantilla/Sevilla','https://www.resultados-futbol.com/plantilla/Real-Sociedad',
'https://www.resultados-futbol.com/plantilla/Valencia-Cf','https://www.resultados-futbol.com/plantilla/Villarreal',
'https://www.resultados-futbol.com/plantilla/Athletic-Bilbao','https://www.resultados-futbol.com/plantilla/Huesca',
'https://www.resultados-futbol.com/plantilla/Levante','https://www.resultados-futbol.com/plantilla/Rayo-Vallecano',
'https://www.resultados-futbol.com/plantilla/Betis','https://www.resultados-futbol.com/plantilla/Alaves',
'https://www.resultados-futbol.com/plantilla/Valladolid','https://www.resultados-futbol.com/plantilla/Eibar',
'https://www.resultados-futbol.com/plantilla/Celta','https://www.resultados-futbol.com/plantilla/Girona-Fc',
'https://www.resultados-futbol.com/plantilla/Leganes','https://www.resultados-futbol.com/plantilla/Espanyol']


equipos=['Real Madrid','Barcelona','Getafe','Atlético Madrid','Sevilla','Real Sociedad','Valencia','Villarreal',
'Athletic Bilbao','Huesca','Levante','Rayo Vallecano','Real Betis','Alavés','Real Valladolid','Eibar','Celta de Vigo','Girona',
'Leganés','Espanyol']

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
	
	#URL='https://www.resultados-futbol.com/plantilla/Real-Madrid'
	#temporada 2018/2019
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

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_españa_2018_2019.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])

ulrs=['https://www.resultados-futbol.com/plantilla/Real-Madrid', 'https://www.resultados-futbol.com/plantilla/Barcelona',
'https://www.resultados-futbol.com/plantilla/Getafe', 'https://www.resultados-futbol.com/plantilla/Atletico-Madrid',
'https://www.resultados-futbol.com/plantilla/Sevilla','https://www.resultados-futbol.com/plantilla/Real-Sociedad',
'https://www.resultados-futbol.com/plantilla/Valencia-Cf','https://www.resultados-futbol.com/plantilla/Villarreal',
'https://www.resultados-futbol.com/plantilla/Athletic-Bilbao','https://www.resultados-futbol.com/plantilla/Malaga',
'https://www.resultados-futbol.com/plantilla/Levante','https://www.resultados-futbol.com/plantilla/Deportivo',
'https://www.resultados-futbol.com/plantilla/Betis','https://www.resultados-futbol.com/plantilla/Alaves',
'https://www.resultados-futbol.com/plantilla/Ud-Palmas','https://www.resultados-futbol.com/plantilla/Eibar',
'https://www.resultados-futbol.com/plantilla/Celta','https://www.resultados-futbol.com/plantilla/Girona-Fc',
'https://www.resultados-futbol.com/plantilla/Leganes','https://www.resultados-futbol.com/plantilla/Espanyol']

equipos=['Real Madrid','Barcelona','Getafe','Atlético Madrid','Sevilla','Real Sociedad','Valencia','Villarreal',
'Athletic Bilbao','Málaga','Levante','Deportivo','Real Betis','Alavés','Las Palmas','Eibar','Celta de Vigo','Girona',
'Leganés','Espanyol']

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
	#temporada 2017/2018
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

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_españa_2017_2018.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])


ulrs=['https://www.resultados-futbol.com/plantilla/Real-Madrid', 'https://www.resultados-futbol.com/plantilla/Barcelona',
'https://www.resultados-futbol.com/plantilla/Granada', 'https://www.resultados-futbol.com/plantilla/Atletico-Madrid',
'https://www.resultados-futbol.com/plantilla/Sevilla','https://www.resultados-futbol.com/plantilla/Real-Sociedad',
'https://www.resultados-futbol.com/plantilla/Valencia-Cf','https://www.resultados-futbol.com/plantilla/Villarreal',
'https://www.resultados-futbol.com/plantilla/Athletic-Bilbao','https://www.resultados-futbol.com/plantilla/Malaga',
'https://www.resultados-futbol.com/plantilla/Sporting-Gijon','https://www.resultados-futbol.com/plantilla/Deportivo',
'https://www.resultados-futbol.com/plantilla/Betis','https://www.resultados-futbol.com/plantilla/Alaves',
'https://www.resultados-futbol.com/plantilla/Ud-Palmas','https://www.resultados-futbol.com/plantilla/Eibar',
'https://www.resultados-futbol.com/plantilla/Celta','https://www.resultados-futbol.com/plantilla/Osasuna',
'https://www.resultados-futbol.com/plantilla/Leganes','https://www.resultados-futbol.com/plantilla/Espanyol']

equipos=['Real Madrid','Barcelona','Granada','Atlético Madrid','Sevilla','Real Sociedad','Valencia','Villarreal',
'Athletic Bilbao','Málaga','Real Sporting','Deportivo','Real Betis','Alavés','Las Palmas','Eibar','Celta de Vigo','Osasuna',
'Leganés','Espanyol']

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
	#temporada 2016/2017
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

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_españa_2016_2017.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])


