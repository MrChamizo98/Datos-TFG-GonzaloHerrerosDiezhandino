#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import csv
import re
from bs4 import BeautifulSoup

class Champions:
	temporada=""
	grupo=""
	fecha=""
	local=""
	visitante=""
	resultado=""

#TEMPORADA ACTUAL
urls=['https://www.resultados-futbol.com/champions2020/','https://www.resultados-futbol.com/champions2019/',
'https://www.resultados-futbol.com/champions2018/','https://www.resultados-futbol.com/champions2017/']

temporadas=['Temporada2020','Temporada2019','Temporada2018','Temporada2017']
#URL='https://www.resultados-futbol.com/champions2020/'

#TEMPORADA 2018/2019
#URL='https://resultados.as.com/resultados/futbol/primera/2018_2019/clasificacion/'

#TEMPORADA 2017/2018
#URL='https://resultados.as.com/resultados/futbol/primera/2017_2018/clasificacion/'

#TEMPORADA 2016/2017
#URL='https://resultados.as.com/resultados/futbol/primera/2016_2017/clasificacion/'

lista=[]

j=Champions()
j.temporada="champions_temporada"
j.grupo="champions_grupo"
j.fecha="champions_fecha"
j.local="champions_local"
j.visitante="champions_visitante"
j.resultado="champions_resultado"
lista.append(j)

itera=0

for URL in urls:

	temporada=temporadas[itera]

	for i in range(0,9):

		page = requests.get(URL+'grupo'+str(i)+'/calendario')
			
		grupo="Grupo "+str(i)

		soup=BeautifulSoup(page.content,'html.parser')

		results=soup.find('div',class_='b2col-container col-calendar-content')
		#print(len(results))
		#print(results.prettify())
		partidos=results.find_all('tr')

		for partido in partidos:
			fecha=partido.find('td',class_='fecha')
			local=partido.find('td',class_='equipo1')
			visitante=partido.find('td',class_='equipo2')
			resultado=partido.find('td',class_='rstd')
			resultado=resultado.find('a')

			fecha=fecha.text.encode('utf-8').strip()
			local=local.text.encode('utf-8').strip()
			visitante=visitante.text.encode('utf-8').strip()
			if resultado is None:
				resultado=""
			else:
				resultado=resultado.text.encode('utf-8').strip()

			if local == "Athletic":
				local="Athletic Bilbao"
			if local == "Atlético":
				local="Atlético Madrid"
			if local == "Celta":
				local="Celta de Vigo"
			if local == "R. Sociedad":
				local="Real Sociedad"

			if visitante == "Athletic":
				visitante="Athletic Bilbao"
			if visitante == "Atlético":
				visitante="Atlético Madrid"
			if visitante == "Celta":
				visitante="Celta de Vigo"
			if visitante == "R. Sociedad":
				visitante="Real Sociedad"

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

			if local =="Hellas":
				local="Hellas Verona"
			if local == "Palermo":
				local="SSD Palermo"

			if visitante =="Hellas":
				visitante="Hellas Verona"
			if visitante == "Palermo":
				visitante="SSD Palermo"

				
			if local=="Bayern":
				local="Bayern München"
			if local == "Dortmund":
				local="B. Dortmund"
			if local == "Augsburg":
				local="FC Augsburg"
			if local=="Leverkusen":
				local="B. Leverkusen"
			if local=="Monchenglad":
				local="Monchengladbach"
			if local == "Werder":
				local="Werder Bremen"
			if local=="Freiburg":
				local="SC Freiburg"
			if local == "Union":
				local="Union Berlin"
			if local=="Hannover":
				local="Hannover 96"
			if local=="Hamburger":
				local="Hamburguer SV"
			if local=="Inglostadt":
				local="Inglostadt 04"
			if local=="Darmstadt":
				local="Darmstadt 98"
			if local=="B. Monchengladbach":
				local="Monchengladbach"
			if local=="Fortuna Düsseldorf":
				local="Fortuna"
			if local=="Eintracht Frankfurt":
				local="Eintracht"


			if visitante=="Bayern":
				visitante="Bayern München"
			if visitante == "Dortmund":
				visitante="B. Dortmund"
			if visitante == "Augsburg":
				visitante="FC Augsburg"
			if visitante=="Leverkusen":
				visitante="B. Leverkusen"
			if visitante=="Monchenglad":
				visitante="Monchengladbach"
			if visitante == "Werder":
				visitante="Werder Bremen"
			if visitante=="Freiburg":
				visitante="SC Freiburg"
			if visitante == "Union":
				visitante="Union Berlin"
			if visitante=="Hannover":
				visitante="Hannover 96"
			if visitante=="Hamburger":
				visitante="Hamburguer SV"
			if visitante=="Inglostadt":
				visitante="Inglostadt 04"
			if visitante=="Darmstadt":
				visitante="Darmstadt 98"
			if visitante=="B. Monchengladbach":
				visitante="Monchengladbach"
			if visitante=="Fortuna Düsseldorf":
				visitante="Fortuna"
			if visitante=="Eintracht Frankfurt":
				visitante="Eintracht"

			j=Champions()
			j.temporada=temporada
			j.grupo=grupo
			j.fecha=fecha
			j.local=local
			j.visitante=visitante
			j.resultado=resultado
			lista.append(j)
	itera=itera+1


csvfile="/home/gonzalo/Escritorio/TFG/CHAMPIONS-COPA-UEFA/calendario_champions.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.grupo,val.fecha,val.local,val.visitante,val.resultado])










