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
urls=['https://www.resultados-futbol.com/capital_one_cup2020/grupo0/calendario',
'https://www.resultados-futbol.com/capital_one_cup2019/grupo0/calendario',
'https://www.resultados-futbol.com/capital_one_cup2018/grupo0/calendario',
'https://www.resultados-futbol.com/capital_one_cup2017/grupo0/calendario']

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

		if local == "Brighton":
			local="Brighton Hove A."
		if local == "Bournemouth":
			local = "AFC Bournemouth"
		if local == "Sheffield":
			local = "Sheffield United"
		if local == "Crystal":
			local = "Crystal Palace"
		if local == "Norwich":
			local = "Norwich City"
		if local == "West":
			local = "West Bromwich A."
		if local == "Swansea":
			local = "Swansea City"
		if local =="Middlesbrou":
			local="Middlesbrough"
		if local=="Cardiff":
			local="Cardiff City"
		if local =="Brighton & Hove Albion":
			local="Brighton Hove A."
		if local=="Tottenham Hotspur":
			local="Tottenham"
		if local=="Bournemouth FC":
			local="AFC Bournemouth"
		if local=="Huddersfield Town":
			local="Huddersfield"
		if local=="West Bromwich Albion":
			local="West Bromwich A."

		if visitante == "Brighton":
			visitante="Brighton Hove A."
		if visitante == "Bournemouth":
			visitante = "AFC Bournemouth"
		if visitante == "Sheffield":
			visitante = "Sheffield United"
		if visitante == "Crystal":
			visitante = "Crystal Palace"
		if visitante == "Norwich":
			visitante = "Norwich City"
		if visitante == "West":
			visitante = "West Bromwich A."
		if visitante == "Swansea":
			visitante = "Swansea City"
		if visitante =="Middlesbrou":
			visitante="Middlesbrough"
		if visitante=="Cardiff":
			visitante="Cardiff City"
		if visitante =="Brighton & Hove Albion":
			visitante="Brighton Hove A."
		if visitante=="Tottenham Hotspur":
			visitante="Tottenham"
		if visitante=="Bournemouth FC":
			visitante="AFC Bournemouth"
		if visitante=="Huddersfield Town":
			visitante="Huddersfield"
		if visitante=="West Bromwich Albion":
			visitante="West Bromwich A."

		j=Copa()
		j.temporada=temporada
		j.fecha=fecha
		j.local=local
		j.visitante=visitante
		j.resultado=resultado
		lista.append(j)

	itera=itera+1

csvfile="/home/gonzalo/Escritorio/TFG/CHAMPIONS-COPA-UEFA/calendario_carabao.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.fecha,val.local,val.visitante,val.resultado])










