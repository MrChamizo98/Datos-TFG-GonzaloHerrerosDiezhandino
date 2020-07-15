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


ulrs=['https://www.resultados-futbol.com/plantilla/Juventus-Fc', 'https://www.resultados-futbol.com/plantilla/Lazio',
'https://www.resultados-futbol.com/plantilla/Internazionale', 'https://www.resultados-futbol.com/plantilla/Atalanta',
'https://www.resultados-futbol.com/plantilla/Roma','https://www.resultados-futbol.com/plantilla/Napoli',
'https://www.resultados-futbol.com/plantilla/Milan','https://www.resultados-futbol.com/plantilla/Hellas-Verona-Fc',
'https://www.resultados-futbol.com/plantilla/Parma-Fc','https://www.resultados-futbol.com/plantilla/Bologna',
'https://www.resultados-futbol.com/plantilla/Us-Sassuolo-Calcio','https://www.resultados-futbol.com/plantilla/Cagliari',
'https://www.resultados-futbol.com/plantilla/Fiorentina','https://www.resultados-futbol.com/plantilla/Udinese',
'https://www.resultados-futbol.com/plantilla/Torino-Fc','https://www.resultados-futbol.com/plantilla/Sampdoria',
'https://www.resultados-futbol.com/plantilla/Genoa','https://www.resultados-futbol.com/plantilla/Lecce',
'https://www.resultados-futbol.com/plantilla/Spal-1907','https://www.resultados-futbol.com/plantilla/Brescia']


equipos=['Juventus','Lazio','Inter', 'Atalanta','Roma','Napoli','Milan','Hellas Verona','Parma','Bologna','Sassuolo',
'Cagliari','Fiorentina','Udinese','Torino','Sampdoria','Genoa', 'Lecce','SPAL','Brescia']

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

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_seriea_2019_2020.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])


ulrs=['https://www.resultados-futbol.com/plantilla/Juventus-Fc', 'https://www.resultados-futbol.com/plantilla/Lazio',
'https://www.resultados-futbol.com/plantilla/Internazionale', 'https://www.resultados-futbol.com/plantilla/Atalanta',
'https://www.resultados-futbol.com/plantilla/Roma','https://www.resultados-futbol.com/plantilla/Napoli',
'https://www.resultados-futbol.com/plantilla/Milan','https://www.resultados-futbol.com/plantilla/Empoli-Fc',
'https://www.resultados-futbol.com/plantilla/Parma-Fc','https://www.resultados-futbol.com/plantilla/Bologna',
'https://www.resultados-futbol.com/plantilla/Us-Sassuolo-Calcio','https://www.resultados-futbol.com/plantilla/Cagliari',
'https://www.resultados-futbol.com/plantilla/Fiorentina','https://www.resultados-futbol.com/plantilla/Udinese',
'https://www.resultados-futbol.com/plantilla/Torino-Fc','https://www.resultados-futbol.com/plantilla/Sampdoria',
'https://www.resultados-futbol.com/plantilla/Genoa','https://www.resultados-futbol.com/plantilla/Frosinone-Calcio',
'https://www.resultados-futbol.com/plantilla/Spal-1907','https://www.resultados-futbol.com/plantilla/Chievo']


equipos=['Juventus','Lazio','Inter', 'Atalanta','Roma','Napoli','Milan','Empoli','Parma','Bologna','Sassuolo',
'Cagliari','Fiorentina','Udinese','Torino','Sampdoria','Genoa', 'Frosinone','SPAL','Chievo']
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

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_seriea_2018_2019.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])

ulrs=['https://www.resultados-futbol.com/plantilla/Juventus-Fc', 'https://www.resultados-futbol.com/plantilla/Lazio',
'https://www.resultados-futbol.com/plantilla/Internazionale', 'https://www.resultados-futbol.com/plantilla/Atalanta',
'https://www.resultados-futbol.com/plantilla/Roma','https://www.resultados-futbol.com/plantilla/Napoli',
'https://www.resultados-futbol.com/plantilla/Milan','https://www.resultados-futbol.com/plantilla/Fc-Crotone',
'https://www.resultados-futbol.com/plantilla/Hellas-Verona-Fc','https://www.resultados-futbol.com/plantilla/Bologna',
'https://www.resultados-futbol.com/plantilla/Us-Sassuolo-Calcio','https://www.resultados-futbol.com/plantilla/Cagliari',
'https://www.resultados-futbol.com/plantilla/Fiorentina','https://www.resultados-futbol.com/plantilla/Udinese',
'https://www.resultados-futbol.com/plantilla/Torino-Fc','https://www.resultados-futbol.com/plantilla/Sampdoria',
'https://www.resultados-futbol.com/plantilla/Genoa','https://www.resultados-futbol.com/plantilla/Benevento-Calcio',
'https://www.resultados-futbol.com/plantilla/Spal-1907','https://www.resultados-futbol.com/plantilla/Chievo']


equipos=['Juventus','Lazio','Inter', 'Atalanta','Roma','Napoli','Milan','Crotone','Hellas Verona','Bologna','Sassuolo',
'Cagliari','Fiorentina','Udinese','Torino','Sampdoria','Genoa','Benevento' ,'SPAL','Chievo']
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

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_seriea_2017_2018.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])


ulrs=['https://www.resultados-futbol.com/plantilla/Juventus-Fc', 'https://www.resultados-futbol.com/plantilla/Lazio',
'https://www.resultados-futbol.com/plantilla/Internazionale', 'https://www.resultados-futbol.com/plantilla/Atalanta',
'https://www.resultados-futbol.com/plantilla/Roma','https://www.resultados-futbol.com/plantilla/Napoli',
'https://www.resultados-futbol.com/plantilla/Milan','https://www.resultados-futbol.com/plantilla/Fc-Crotone',
'https://www.resultados-futbol.com/plantilla/Empoli-Fc','https://www.resultados-futbol.com/plantilla/Bologna',
'https://www.resultados-futbol.com/plantilla/Us-Sassuolo-Calcio','https://www.resultados-futbol.com/plantilla/Cagliari',
'https://www.resultados-futbol.com/plantilla/Fiorentina','https://www.resultados-futbol.com/plantilla/Udinese',
'https://www.resultados-futbol.com/plantilla/Torino-Fc','https://www.resultados-futbol.com/plantilla/Sampdoria',
'https://www.resultados-futbol.com/plantilla/Genoa','https://www.resultados-futbol.com/plantilla/Palermo',
'https://www.resultados-futbol.com/plantilla/Pescara-Calcio','https://www.resultados-futbol.com/plantilla/Chievo']


equipos=['Juventus','Lazio','Inter', 'Atalanta','Roma','Napoli','Milan','Crotone','Empoli','Bologna','Sassuolo',
'Cagliari','Fiorentina','Udinese','Torino','Sampdoria','Genoa','SSD Palermo','Pescara','Chievo']
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

csvfile="/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_seriea_2016_2017.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.equipo,val.dorsal,val.foto,val.nombre,val.posicion,val.edad,val.pais,val.altura,val.peso,val.goles,val.rojas,val.amarillas])

