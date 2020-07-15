#!/usr/bin/python
# -*- coding: ascii -*-
import os, sys
import requests
import csv
import re
from bs4 import BeautifulSoup
import csv

class Alineacion:
	jugador=""
	amarilla=""
	roja=""
	gol=""
	cambio=""
	estado=""
	equipo=""
	jornada=""
	lesion=""
	asistencia=""

a=Alineacion()
a.jugador="Jugador"
a.amarilla="Amarilla"
a.roja="Roja"
a.gol="Gol"
a.cambio="Cambio"
a.estado="Estado"
a.equipo="Equipo"
a.jornada="Jornada"
a.lesion="Lesion"
a.asistencia="Asistencia"

lista=[]
lista.append(a)

URL='https://www.resultados-futbol.com/partido/Osasuna/Real-Madrid'
page = requests.get(URL)


soup=BeautifulSoup(page.content,'html.parser')

jornada=soup.find('div',class_='jornada')
jornada=jornada.text.encode('utf-8').strip()

dat=jornada.split(" ")

equipo_local=soup.find('div',class_='team team1')
local=equipo_local.find('h3',class_='nteam nteam1')
local=local.text.encode('utf-8').strip()
equipo_visitante=soup.find('div',class_='team team2')
visitante=equipo_visitante.find('h3',class_='nteam nteam2')
visitante=visitante.text.encode('utf-8').strip()
print(dat[1])


lesion=0
asistencia=0

local_lesion=soup.find_all('span',class_="left event_4")
local_asistencias=soup.find_all('span',class_="left event_5")
visitante_lesion=soup.find_all('span',class_="right event_4")
visitante_asistencia=soup.find_all('span',class_="right event_5")

lesiones_local=[]
for a in local_lesion:
	nombre=a.find('a')
	lesiones_local.append(nombre.text.encode('utf-8').strip())

asistencia_local=[]
for a in local_asistencias:
	nombre=a.find('a')
	asistencia_local.append(nombre.text.encode('utf-8').strip())

lesiones_visitante=[]
for a in visitante_lesion:
	nombre=a.find('a')
	lesiones_visitante.append(nombre.text.encode('utf-8').strip())

asistencia_visitante=[]
for a in visitante_asistencia:
	nombre=a.find('a')
	asistencia_visitante.append(nombre.text.encode('utf-8').strip())


#locales
equipo_local=equipo_local.find_all('li',class_='')
i=0
for jugador in equipo_local:
	if i<11:
		estado="Titular"
	else:
		estado="Suplente"
	i=i+1
	nombre=jugador.find('h5',class_='align-player')
	eventos=jugador.find('div',class_='align-events')
	if None is eventos:
		continue
	if eventos.find('span',class_='flaticon-live-5'):
		amarilla="1"
	else:
		amarilla="0"
	if eventos.find('span',class_='flaticon-goal'):
		gol=eventos.find('span',class_='flaticon-goal')
		if gol.find('b',class_=''):
			gol=gol.find('b',class_='')
			gol=gol.text.encode('utf-8').strip()
		else:
			gol="1"
	else:
		gol="0"
	if eventos.find('span',class_='flaticon-up12'):
		cambio=eventos.find('span',class_='flaticon-up12')
		cambio=cambio.text.encode('utf-8').strip()
	else:
		cambio=""
	if eventos.find('span',class_='flaticon-live-3'):
		roja="1"
	else:
		roja="0"

	nombre=nombre.text.encode('utf-8').strip()
	lesion=0
	for a in lesiones_local:
		if a == nombre:
			print('entra bucle')
			lesion=1
	asistencia=0
	for a in asistencia_local:
		if a == nombre:
			print('entra bucle')
			asistencia=asistencia+1

	j=Alineacion()
	j.jugador=nombre
	j.estado=estado
	j.amarilla=amarilla
	j.gol=gol
	j.cambio=cambio[:2]
	j.roja=roja
	j.jornada=jornada
	j.equipo=local
	j.lesion=lesion
	j.asistencia=asistencia
	lista.append(j)


#visitantes
equipo_visitante=equipo_visitante.find_all('li',class_='')
i=0
for jugador in equipo_visitante:
	if i<11:
		estado="Titular"
	else:
		estado="Suplente"
	i=i+1
	nombre=jugador.find('h5',class_='align-player')
	eventos=jugador.find('div',class_='align-events')
	if None is eventos:
		continue
	if eventos.find('span',class_='flaticon-live-5'):
		amarilla="1"
	else:
		amarilla="0"
	if eventos.find('span',class_='flaticon-goal'):
		gol=eventos.find('span',class_='flaticon-goal')
		if gol.find('b',class_=''):
			gol=gol.find('b',class_='')
			gol=gol.text.encode('utf-8').strip()
		else:
			gol="1"
	else:
		gol="0"
	if eventos.find('span',class_='flaticon-up12'):
		cambio=eventos.find('span',class_='flaticon-up12')
		cambio=cambio.text.encode('utf-8').strip()
	else:
		cambio=""
	if eventos.find('span',class_='flaticon-live-3'):
		roja="1"
	else:
		roja="0"

	nombre=nombre.text.encode('utf-8').strip()
	lesion=0
	for a in lesiones_visitante:
		if a == nombre:
			print('entra bucle')
			lesion=1
	asistencia=0
	for a in asistencia_visitante:
		if a == nombre:
			print('entra bucle')
			asistencia=asistencia+1

	j=Alineacion()
	j.jugador=nombre
	j.estado=estado
	j.amarilla=amarilla
	j.gol=gol
	j.cambio=cambio[:2]
	j.roja=roja
	j.jornada=jornada
	j.equipo=visitante
	j.lesion=lesion
	j.asistencia=asistencia
	lista.append(j)

csvfile="/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_osasuna_realmadrid.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.jornada,val.equipo,val.jugador,val.estado,val.cambio,val.gol,val.amarilla,val.roja,val.asistencia,val.lesion])














