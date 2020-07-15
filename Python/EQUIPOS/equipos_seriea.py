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


ulrs=['https://www.resultados-futbol.com/Juventus-Fc', 'https://www.resultados-futbol.com/Lazio',
'https://www.resultados-futbol.com/Internazionale', 'https://www.resultados-futbol.com/Atalanta',
'https://www.resultados-futbol.com/Roma','https://www.resultados-futbol.com/Napoli',
'https://www.resultados-futbol.com/Milan','https://www.resultados-futbol.com/Hellas-Verona-Fc',
'https://www.resultados-futbol.com/Parma-Fc','https://www.resultados-futbol.com/Bologna',
'https://www.resultados-futbol.com/Us-Sassuolo-Calcio','https://www.resultados-futbol.com/Cagliari',
'https://www.resultados-futbol.com/Fiorentina','https://www.resultados-futbol.com/Udinese',
'https://www.resultados-futbol.com/Torino-Fc','https://www.resultados-futbol.com/Sampdoria',
'https://www.resultados-futbol.com/Genoa','https://www.resultados-futbol.com/Lecce',
'https://www.resultados-futbol.com/Spal-1907','https://www.resultados-futbol.com/Brescia']


equipos=['Juventus','Lazio','Inter', 'Atalanta','Roma','Napoli','Milan','Hellas Verona','Parma','Bologna','Sassuolo',
'Cagliari','Fiorentina','Udinese','Torino','Sampdoria','Genoa', 'Lecce','SPAL','Brescia']

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
	
	

ulrs=['https://www.resultados-futbol.com/Juventus-Fc', 'https://www.resultados-futbol.com/Lazio',
'https://www.resultados-futbol.com/Internazionale', 'https://www.resultados-futbol.com/Atalanta',
'https://www.resultados-futbol.com/Roma','https://www.resultados-futbol.com/Napoli',
'https://www.resultados-futbol.com/Milan','https://www.resultados-futbol.com/Empoli-Fc',
'https://www.resultados-futbol.com/Parma-Fc','https://www.resultados-futbol.com/Bologna',
'https://www.resultados-futbol.com/Us-Sassuolo-Calcio','https://www.resultados-futbol.com/Cagliari',
'https://www.resultados-futbol.com/Fiorentina','https://www.resultados-futbol.com/Udinese',
'https://www.resultados-futbol.com/Torino-Fc','https://www.resultados-futbol.com/Sampdoria',
'https://www.resultados-futbol.com/Genoa','https://www.resultados-futbol.com/Frosinone-Calcio',
'https://www.resultados-futbol.com/Spal-1907','https://www.resultados-futbol.com/Chievo']


equipos=['Juventus','Lazio','Inter', 'Atalanta','Roma','Napoli','Milan','Empoli','Parma','Bologna','Sassuolo',
'Cagliari','Fiorentina','Udinese','Torino','Sampdoria','Genoa', 'Frosinone','SPAL','Chievo']

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
	
	

ulrs=['https://www.resultados-futbol.com/Juventus-Fc', 'https://www.resultados-futbol.com/Lazio',
'https://www.resultados-futbol.com/Internazionale', 'https://www.resultados-futbol.com/Atalanta',
'https://www.resultados-futbol.com/Roma','https://www.resultados-futbol.com/Napoli',
'https://www.resultados-futbol.com/Milan','https://www.resultados-futbol.com/Fc-Crotone',
'https://www.resultados-futbol.com/Hellas-Verona-Fc','https://www.resultados-futbol.com/Bologna',
'https://www.resultados-futbol.com/Us-Sassuolo-Calcio','https://www.resultados-futbol.com/Cagliari',
'https://www.resultados-futbol.com/Fiorentina','https://www.resultados-futbol.com/Udinese',
'https://www.resultados-futbol.com/Torino-Fc','https://www.resultados-futbol.com/Sampdoria',
'https://www.resultados-futbol.com/Genoa','https://www.resultados-futbol.com/Benevento-Calcio',
'https://www.resultados-futbol.com/Spal-1907','https://www.resultados-futbol.com/Chievo']


equipos=['Juventus','Lazio','Inter', 'Atalanta','Roma','Napoli','Milan','Crotone','Hellas Verona','Bologna','Sassuolo',
'Cagliari','Fiorentina','Udinese','Torino','Sampdoria','Genoa','Benevento' ,'SPAL','Chievo']


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
	
	


ulrs=['https://www.resultados-futbol.com/Juventus-Fc', 'https://www.resultados-futbol.com/Lazio',
'https://www.resultados-futbol.com/Internazionale', 'https://www.resultados-futbol.com/Atalanta',
'https://www.resultados-futbol.com/Roma','https://www.resultados-futbol.com/Napoli',
'https://www.resultados-futbol.com/Milan','https://www.resultados-futbol.com/Fc-Crotone',
'https://www.resultados-futbol.com/Empoli-Fc','https://www.resultados-futbol.com/Bologna',
'https://www.resultados-futbol.com/Us-Sassuolo-Calcio','https://www.resultados-futbol.com/Cagliari',
'https://www.resultados-futbol.com/Fiorentina','https://www.resultados-futbol.com/Udinese',
'https://www.resultados-futbol.com/Torino-Fc','https://www.resultados-futbol.com/Sampdoria',
'https://www.resultados-futbol.com/Genoa','https://www.resultados-futbol.com/Palermo',
'https://www.resultados-futbol.com/Pescara-Calcio','https://www.resultados-futbol.com/Chievo']


equipos=['Juventus','Lazio','Inter', 'Atalanta','Roma','Napoli','Milan','Crotone','Empoli','Bologna','Sassuolo',
'Cagliari','Fiorentina','Udinese','Torino','Sampdoria','Genoa','SSD Palermo','Pescara','Chievo']

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
	
	

	
csvfile="/home/gonzalo/Escritorio/TFG/EQUIPOS/equipos_seriea.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')
	for val in lista:
		writer.writerow([val.temporada,val.foto,val.nombre,val.estadio,val.entrenador,val.ubicacion])




