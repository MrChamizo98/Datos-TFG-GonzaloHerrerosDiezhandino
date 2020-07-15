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


ulrs=['https://www.resultados-futbol.com/Bayern-Munchen', 'https://www.resultados-futbol.com/Borussia-Dortmund',
'https://www.resultados-futbol.com/Rb-Leipzig', 'https://www.resultados-futbol.com/Borussia-Monchengla',
'https://www.resultados-futbol.com/Bayer-Leverkusen','https://www.resultados-futbol.com/Schalke-04',
'https://www.resultados-futbol.com/Wolfsburg','https://www.resultados-futbol.com/Sc-Freiburg',
'https://www.resultados-futbol.com/Tsg-1899-Hoffenheim','https://www.resultados-futbol.com/1-Fc-Koln',
'https://www.resultados-futbol.com/1-Fc-Union-Berlin','https://www.resultados-futbol.com/Eintracht-Frankfurt',
'https://www.resultados-futbol.com/Hertha-Bsc','https://www.resultados-futbol.com/Fc-Augsburg',
'https://www.resultados-futbol.com/Mainz-Amat','https://www.resultados-futbol.com/Fortuna-Dusseldorf',
'https://www.resultados-futbol.com/Werder-Bremen','https://www.resultados-futbol.com/Paderborn']


equipos=['Bayern München','B. Dortmund', 'RB Leipzig','Monchengladbach','B. Leverkusen','Schalke 04', 'Wolfsburg', 'SC Freiburg',
'Hoffenheim', 'Köln', 'Union Berlin', 'Eintracht', 'Hertha BSC', 'FC Augsburg', 'Mainz 05', 'Fortuna', 'Werder Bremen', 'Paderborn']

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
	
	


ulrs=['https://www.resultados-futbol.com/Bayern-Munchen', 'https://www.resultados-futbol.com/Borussia-Dortmund',
'https://www.resultados-futbol.com/Rb-Leipzig', 'https://www.resultados-futbol.com/Borussia-Monchengla',
'https://www.resultados-futbol.com/Bayer-Leverkusen','https://www.resultados-futbol.com/Schalke-04',
'https://www.resultados-futbol.com/Wolfsburg','https://www.resultados-futbol.com/Sc-Freiburg',
'https://www.resultados-futbol.com/Tsg-1899-Hoffenheim','https://www.resultados-futbol.com/Stuttgart',
'https://www.resultados-futbol.com/Hannover-96','https://www.resultados-futbol.com/Eintracht-Frankfurt',
'https://www.resultados-futbol.com/Hertha-Bsc','https://www.resultados-futbol.com/Fc-Augsburg',
'https://www.resultados-futbol.com/Mainz-Amat','https://www.resultados-futbol.com/Fortuna-Dusseldorf',
'https://www.resultados-futbol.com/Werder-Bremen','https://www.resultados-futbol.com/Fc-Nurnberg']


equipos=['Bayern München','B. Dortmund', 'RB Leipzig','Monchengladbach','B. Leverkusen','Schalke 04', 'Wolfsburg', 'SC Freiburg',
'Hoffenheim', 'Stuttgart', 'Hannover 96', 'Eintracht', 'Hertha BSC', 'FC Augsburg', 'Mainz 05', 'Fortuna', 'Werder Bremen', 'Nürnberg']

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
	
	

	
ulrs=['https://www.resultados-futbol.com/Bayern-Munchen', 'https://www.resultados-futbol.com/Borussia-Dortmund',
'https://www.resultados-futbol.com/Rb-Leipzig', 'https://www.resultados-futbol.com/Borussia-Monchengla',
'https://www.resultados-futbol.com/Bayer-Leverkusen','https://www.resultados-futbol.com/Schalke-04',
'https://www.resultados-futbol.com/Wolfsburg','https://www.resultados-futbol.com/Sc-Freiburg',
'https://www.resultados-futbol.com/Tsg-1899-Hoffenheim','https://www.resultados-futbol.com/Stuttgart',
'https://www.resultados-futbol.com/Hannover-96','https://www.resultados-futbol.com/Eintracht-Frankfurt',
'https://www.resultados-futbol.com/Hertha-Bsc','https://www.resultados-futbol.com/Fc-Augsburg',
'https://www.resultados-futbol.com/Mainz-Amat','https://www.resultados-futbol.com/1-Fc-Koln',
'https://www.resultados-futbol.com/Werder-Bremen','https://www.resultados-futbol.com/Hamburger-Sv']


equipos=['Bayern München','B. Dortmund', 'RB Leipzig','Monchengladbach','B. Leverkusen','Schalke 04', 'Wolfsburg', 'SC Freiburg',
'Hoffenheim', 'Stuttgart', 'Hannover 96', 'Eintracht', 'Hertha BSC', 'FC Augsburg', 'Mainz 05', 'Köln', 'Werder Bremen', 'Hamburger SV']

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
	
	


ulrs=['https://www.resultados-futbol.com/Bayern-Munchen', 'https://www.resultados-futbol.com/Borussia-Dortmund',
'https://www.resultados-futbol.com/Rb-Leipzig', 'https://www.resultados-futbol.com/Borussia-Monchengla',
'https://www.resultados-futbol.com/Bayer-Leverkusen','https://www.resultados-futbol.com/Schalke-04',
'https://www.resultados-futbol.com/Wolfsburg','https://www.resultados-futbol.com/Sc-Freiburg',
'https://www.resultados-futbol.com/Tsg-1899-Hoffenheim','https://www.resultados-futbol.com/Fc-Ingolstadt-04',
'https://www.resultados-futbol.com/Darmstadt-98','https://www.resultados-futbol.com/Eintracht-Frankfurt',
'https://www.resultados-futbol.com/Hertha-Bsc','https://www.resultados-futbol.com/Fc-Augsburg',
'https://www.resultados-futbol.com/Mainz-Amat','https://www.resultados-futbol.com/1-Fc-Koln',
'https://www.resultados-futbol.com/Werder-Bremen','https://www.resultados-futbol.com/Hamburger-Sv']


equipos=['Bayern München','B. Dortmund', 'RB Leipzig','Monchengladbach','B. Leverkusen','Schalke 04', 'Wolfsburg', 'SC Freiburg',
'Hoffenheim','Ingolstadt 04' ,'Darmstadt 98' , 'Eintracht', 'Hertha BSC', 'FC Augsburg', 'Mainz 05', 'Köln', 'Werder Bremen', 'Hamburger SV']


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
	
	

	
csvfile="/home/gonzalo/Escritorio/TFG/EQUIPOS/equipos_bundesliga.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.foto,val.nombre,val.estadio,val.entrenador,val.ubicacion])




