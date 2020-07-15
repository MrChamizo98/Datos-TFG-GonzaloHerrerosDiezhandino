#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import csv
import re
from bs4 import BeautifulSoup

class Equipo:
	temporada=""
	jornada=""
	posicion=""
	nombre=""
	pjugados=""
	ganados=""
	empatados=""
	perdidos=""
	gfavor=""
	gcontra=""
	puntos=""

	def print_posicion(self):
		print(self.posicion)
	def print_nombre(self):
		print(self.nombre)
	def print_pjugados(self):
		print(self.pjugados)
	def print_ganados(self):
		print(self.ganados)
	def print_empatados(self):
		print(self.empatados)
	def print_perdidos(self):
		print(self.perdidos)
	def print_gfavor(self):
		print(self.gfavor)
	def print_gcontra(self):
		print(self.gcontra)
	def print_puntos(self):
		print(self.puntos)

#TEMPORADA ACTUAL
urls=['https://www.resultados-futbol.com/primera',
'https://www.resultados-futbol.com/primera',
'https://www.resultados-futbol.com/primera',
'https://www.resultados-futbol.com/primera']

#https://www.resultados-futbol.com/primera2019/grupo1/jornada21
temporadas=['Temporada2020','Temporada2019','Temporada2018','Temporada2017']

ano=['2020','2019','2018','2017']
jornadas=39

#URL='https://www.resultados-futbol.com/primera/2019_2020/clasificacion'

#TEMPORADA 2018/2019
#URL='https://resultados.as.com/resultados/futbol/primera/2018_2019/clasificacion/'

#TEMPORADA 2017/2018
#URL='https://resultados.as.com/resultados/futbol/primera/2017_2018/clasificacion/'

#TEMPORADA 2016/2017
#URL='https://resultados.as.com/resultados/futbol/primera/2016_2017/clasificacion/'

lista=[]

j=Equipo()
j.temporada="clasificacion_temporada"
j.jornada="clasificacion_jornada"
j.posicion="clasificacion_posicion"
j.nombre="clasificacion_equipo"
j.puntos="clasificacion_puntos"
j.pjugados="clasificacion_partidos_jugados"
j.ganados="clasificacion_ganados"
j.empatados="clasificacion_empatados"
j.perdidos="clasificacion_perdidos"
j.gfavor="clasificacion_goles_favor"
j.gcontra="clasificacion_goles_contra"
lista.append(j)

itera=0

for URL in urls:
	tempo=temporadas[itera]
	for jornada in range(1,39):
		if requests.get(URL+ano[itera]+'/grupo1/jornada'+str(jornada)):
			page = requests.get(URL+ano[itera]+'/grupo1/jornada'+str(jornada))
		else:
			continue

		soup=BeautifulSoup(page.content,'html.parser')

		results=soup.find('table',id='tabla2')
		results=results.find('tbody')
		#print(len(results))
		#print(results.prettify())

		equipos=results.find_all('tr')
		jor='Jornada '+str(jornada)

		for equipo in equipos:
			nombre=equipo.find('a')
			if None in (nombre):
				continue
			nombre=nombre.text.encode('utf-8').strip()

			puntos=equipo.find(class_='pts')
			puntos=puntos.text.encode('utf-8').strip()

			posicion=equipo.find('th')
			posicion=posicion.text.encode('utf-8').strip()

			pjugados=equipo.find(class_='pj')
			pjugados=pjugados.text.encode('utf-8').strip()

			ganados=equipo.find(class_='win')
			ganados=ganados.text.encode('utf-8').strip()

			empatados=equipo.find(class_='draw')
			empatados=empatados.text.encode('utf-8').strip()

			perdidos=equipo.find(class_='lose')
			perdidos=perdidos.text.encode('utf-8').strip()

			gfavor=equipo.find(class_='f')
			gfavor=gfavor.text.encode('utf-8').strip()

			gcontra=equipo.find(class_='c')
			gcontra=gcontra.text.encode('utf-8').strip()


			if nombre == 'Athletic':
				nombre='Athletic Bilbao'
			if nombre == 'Atlético':
				nombre='Atlético Madrid'
			if nombre == 'Celta':
				nombre='Celta de Vigo'
			if nombre == 'R. Sociedad':
				nombre='Real Sociedad'
			j=Equipo()
			j.temporada=tempo
			j.jornada=jor
			j.posicion=posicion
			j.nombre=nombre
			j.puntos=puntos
			j.pjugados=pjugados
			j.ganados=ganados
			j.empatados=empatados
			j.perdidos=perdidos
			j.gfavor=gfavor
			j.gcontra=gcontra
			lista.append(j)
	itera=itera+1


csvfile="/home/gonzalo/Escritorio/TFG/CLASIFICACION-JORNADA/clasificacion.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.jornada,val.posicion,val.nombre,val.puntos,val.pjugados,val.ganados,val.empatados,val.perdidos,val.gfavor,val.gcontra])










