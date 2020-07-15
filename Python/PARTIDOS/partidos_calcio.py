#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import csv
import re
from bs4 import BeautifulSoup

class Partido:
	temporada=""
	jornada=""
	fecha=""
	local=""
	foto_local=""
	visitante=""
	foto_visitante=""
	resultado=""

urls=['https://www.resultados-futbol.com/serie_a2020/grupo1/calendario',
'https://www.resultados-futbol.com/serie_a2019/grupo1/calendario',
'https://www.resultados-futbol.com/serie_a2018/grupo1/calendario',
'https://www.resultados-futbol.com/serie_a2017/grupo1/calendario']

temporadas=['Temporada2020','Temporada2019','Temporada2018','Temporada2017']
#temporada 2019/2020
#URL='https://www.resultados-futbol.com/primera2020/grupo1/calendario'
#temporada 2018/2019
#URL='https://www.resultados-futbol.com/primera2019/grupo1/calendario'
#temporada 2017/2018
#URL='https://www.resultados-futbol.com/primera2018/grupo1/calendario'
#temporada 2016/2017
#URL='https://www.resultados-futbol.com/primera2017/grupo1/calendario'

p=Partido()
p.temporada='partidos_temporada'
p.jornada='partidos_jornada'
p.fecha='partidos_fecha'
p.local='partidos_equipo_local'
p.foto_local='partidos_foto_local'
p.visitante='partidos_equipo_visitante'
p.foto_visitante='partidos_foto_visitante'
p.resultado="partidos_resultado"

lista=[]
lista.append(p)

itera=0

for a in urls:

	page = requests.get(a)

	soup=BeautifulSoup(page.content,'html.parser')

	results=soup.find('div',class_="b2col-container col-calendar-content")
	jornadas=results.find_all('div',id='col-resultados')


	tempo=temporadas[itera]

	for jornada in jornadas:
		jor=jornada.find('div',class_='boxtop')
		jor=jor.text.encode('utf-8').strip().split("\n")
		jor=jor[3]
		datos=jornada.find_all('tr')
		for i in datos:
			fecha=i.find('td',class_='fecha')
			local=i.find('td',class_='equipo1')
			foto_local=local.find('img').attrs['src']
			if local.text.encode('utf-8').strip() == 'Real':
				local=local.find('img',alt=True)
				local=local['alt']
				local=local.encode('utf-8')
			else:
				local=local.text.encode('utf-8').strip()


			visitante=i.find('td',class_='equipo2')
			foto_visitante=visitante.find('img').attrs['src']
			if visitante.text.encode('utf-8').strip() == 'Real':
				visitante=visitante.find('img',alt=True)
				visitante=visitante['alt']
				visitante=visitante.encode('utf-8')
			else:
				visitante=visitante.text.encode('utf-8').strip()

			resultado=i.find('td',class_='rstd')
			resultado=resultado.find('a',class_='url')

			if local =="Hellas":
				local="Hellas Verona"
			if local == "Palermo":
				local="SSD Palermo"

			if visitante =="Hellas":
				visitante="Hellas Verona"
			if visitante == "Palermo":
				visitante="SSD Palermo"
			p=Partido()
			p.temporada=tempo
			p.jornada=jor
			p.fecha=fecha.text.encode('utf-8').strip()
			p.local=local
			p.visitante=visitante
			p.foto_local=foto_local
			p.foto_visitante=foto_visitante
			if resultado is None:
				p.resultado="Aplazado"
			else:
				p.resultado=resultado.text.encode('utf-8').strip()
			lista.append(p)
	itera=itera+1

csvfile="/home/gonzalo/Escritorio/TFG/PARTIDOS/partidos_serie_a.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.jornada,val.fecha,val.foto_local,val.local,val.resultado,val.foto_visitante,val.visitante])

