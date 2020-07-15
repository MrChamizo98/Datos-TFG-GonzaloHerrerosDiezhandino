#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import csv
import re
from bs4 import BeautifulSoup

class Copa:
	temporada=""
	fecha=""
	local=""
	visitante=""
	resultado=""

#TEMPORADA ACTUAL
urls=['https://www.resultados-futbol.com/coppa_italia2020/grupo0/calendario',
'https://www.resultados-futbol.com/coppa_italia2019/grupo0/calendario',
'https://www.resultados-futbol.com/coppa_italia2018/grupo0/calendario',
'https://www.resultados-futbol.com/coppa_italia2017/grupo0/calendario']

temporadas=['Temporada2020','Temporada2019','Temporada2018','Temporada2017']
#URL='https://www.resultados-futbol.com/copa_del_rey2020/grupo0/calendario'

#TEMPORADA 2018/2019
#URL='https://resultados.as.com/resultados/futbol/primera/2018_2019/clasificacion/'

#TEMPORADA 2017/2018
#URL='https://resultados.as.com/resultados/futbol/primera/2017_2018/clasificacion/'

#TEMPORADA 2016/2017
#URL='https://resultados.as.com/resultados/futbol/primera/2016_2017/clasificacion/'

lista=[]

j=Copa()
j.temporada="copa_temporada"
j.fecha="copa_fecha"
j.local="copa_local"
j.visitante="copa_visitante"
j.resultado="copa_resultado"
lista.append(j)

itera=0

for URL in urls:
	temporada=temporadas[itera]

	page = requests.get(URL)

	soup=BeautifulSoup(page.content,'html.parser')

	results=soup.find('div',class_='b2col-container col-calendar-content')
	#print(len(results))
	#print(results.prettify())
	partidos=results.find_all('tr')

	for partido in partidos:
		fecha=partido.find('td',class_='fecha')
		local=partido.find('td',class_='equipo1')
		visitante=partido.find('td',class_='equipo2')

		local=local.find('img',alt=True)
		local=local['alt']

		visitante=visitante.find('img',alt=True)
		visitante=visitante['alt']

		resultado=partido.find('td',class_='rstd')
		resultado=resultado.find('a')

		fecha=fecha.text.encode('utf-8').strip()
		if resultado is None:
			resultado=""
		else:
			resultado=resultado.text.encode('utf-8').strip()
		local=local.encode('utf-8')
		visitante=visitante.encode('utf-8')

		if local =="Hellas":
			local="Hellas Verona"
		if local == "Palermo":
			local="SSD Palermo"

		if visitante =="Hellas":
			visitante="Hellas Verona"
		if visitante == "Palermo":
			visitante="SSD Palermo"
		j=Copa()
		j.temporada=temporada
		j.fecha=fecha
		j.local=local
		j.visitante=visitante
		j.resultado=resultado
		lista.append(j)

	itera=itera+1

csvfile="/home/gonzalo/Escritorio/TFG/CHAMPIONS-COPA-UEFA/calendario_copa_italia.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.fecha,val.local,val.visitante,val.resultado])










