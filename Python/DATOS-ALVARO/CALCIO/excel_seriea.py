#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import csv
import re
import locale
from bs4 import BeautifulSoup
from datetime import *

class Excel:
	temporada=""
	jornada=""
	local=""
	visitante=""
	resultado=""
	rotacion_titulares=""
	rotacion_suplentes=""
	rotacion_delanteros=""
	rotacion_medios=""
	rotacion_defensas=""
	rotacion_porteros=""
	dias_descanso=""
	rivalidad=""

class jugador:
	equipo=""
	nombre=""
	posicion=""
locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')

plantilla_2019_2020=[]
with open('plantilla_seriea_2019_2020.csv') as csvfile:
	reader_plantilla = csv.DictReader(csvfile)
	for plantilla in reader_plantilla:
		j=jugador()
		j.equipo=plantilla['plantilla_equipo']
		j.nombre=plantilla['plantilla_name']
		j.posicion=plantilla['plantilla_posicion']
		plantilla_2019_2020.append(j)


plantilla_2018_2019=[]
with open('plantilla_seriea_2018_2019.csv') as csvfile:
	reader_plantilla = csv.DictReader(csvfile)
	for plantilla in reader_plantilla:
		j=jugador()
		j.equipo=plantilla['plantilla_equipo']
		j.nombre=plantilla['plantilla_name']
		j.posicion=plantilla['plantilla_posicion']
		plantilla_2018_2019.append(j)


plantilla_2017_2018=[]
with open('plantilla_seriea_2017_2018.csv') as csvfile:
	reader_plantilla = csv.DictReader(csvfile)
	for plantilla in reader_plantilla:
		j=jugador()
		j.equipo=plantilla['plantilla_equipo']
		j.nombre=plantilla['plantilla_name']
		j.posicion=plantilla['plantilla_posicion']
		plantilla_2017_2018.append(j)


plantilla_2016_2017=[]
with open('plantilla_seriea_2016_2017.csv') as csvfile:
	reader_plantilla = csv.DictReader(csvfile)
	for plantilla in reader_plantilla:
		j=jugador()
		j.equipo=plantilla['plantilla_equipo']
		j.nombre=plantilla['plantilla_name']
		j.posicion=plantilla['plantilla_posicion']
		plantilla_2016_2017.append(j)

csvfile="/home/gonzalo/Escritorio/TFG/DATOS-ALVARO/CALCIO/DATOS/datos.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')

	writer.writerow(["TEMPORADA","JORNADA","REFERIDO","LOCAL","VISITANTE","RESULTADO","RIVALIDAD","ROTACION TITULARES","ROTACION SUPLENTES",
					"ROTACION PORTEROS","ROTACION DEFENSAS","ROTACION MEDIOS","ROTACION DELANTEROS","DIAS DESCANSO"])

	with open('partidos_serie_a.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:

				#OBTENEMOS TEMPORADA/JORNADA/LOCAL/VISITANTE/RESULTADO
		        temporada=row['partidos_temporada']
		        jornada=row['partidos_jornada']
		        jor=jornada.split()
		        jor=int(jor[1])
		        jor=jor-1
		        local=row['partidos_equipo_local']
		        visitante=row['partidos_equipo_visitante']
		        resultado=row['partidos_resultado']

		        resultado.split()
  
				
	        	if len(resultado)==7 or len(resultado)==5 or len(resultado)==8:
	        		if len(resultado)==5:
     					resultado_local=resultado
				    	resultado_visitante=resultado
		        	elif resultado[0]=='x': 
				        resultado_local=resultado
				        resultado_visitante=resultado
			        elif len(resultado)==8:
			        	resultado_local=resultado
				    	resultado_visitante=resultado
	     			else:
	     				if int(resultado[0])>int(resultado[6]):
				        	resultado_local="GANADO"
				        	resultado_visitante="PERDIDO"
			         	elif int(resultado[0])==int(resultado[6]):
			         		resultado_local="EMPATADO"
			         		resultado_visitante="EMPATADO"
			     		else:
			     			resultado_local="PERDIDO"
			     			resultado_visitante="GANADO"
	       

				posicion_local=0
				posicion_visitante=0

	 			#OBTENEMOS RIVALIDAD
	 			jornada_pasada="Jornada "+str(jor)
	 			print(jornada+" "+jornada_pasada+resultado_local+"   "+resultado_visitante)
				with open('clasificacion_serie_a.csv') as csvfile:
					reader_rivalidad = csv.DictReader(csvfile)
					for riv in reader_rivalidad:
						if jor==0:
							break
						else:
							if riv['clasificacion_temporada']==temporada and riv['clasificacion_jornada']==jornada_pasada:
								if local==riv['clasificacion_equipo']:
									posicion_local=int(riv['clasificacion_posicion'])
								if visitante==riv['clasificacion_equipo']:
									posicion_visitante=int(riv['clasificacion_posicion'])

				rivalidad_local=posicion_local-posicion_visitante
				rivalidad_visitante=posicion_visitante-posicion_local

				#OBTENEMOS FECHA DE PARTIDO
				fecha=row['partidos_fecha']
				objeto_fecha=datetime.strptime(fecha,'%d %b %y')

				if jor==0:
					fecha_mas_proxima=objeto_fecha
				else:
					fecha_mas_proxima=datetime(2015,6,29)

					with open('calendario_champions.csv') as csvfile:
						reader_champions = csv.DictReader(csvfile)
						for champs in reader_champions:
							if champs['champions_local']==local or champs['champions_visitante']==local:
								fecha_champs=champs['champions_fecha']
								objeto_fecha_champions=datetime.strptime(fecha_champs,'%d %b %y')
								if objeto_fecha_champions>fecha_mas_proxima and objeto_fecha_champions<objeto_fecha:
									fecha_mas_proxima=objeto_fecha_champions

					with open('calendario_uefa.csv') as csvfile:
						reader_uefa = csv.DictReader(csvfile)
						for uefa in reader_uefa:
							if uefa['uefa_local']==local or uefa['uefa_visitante']==local:
								fecha_uefa=uefa['uefa_fecha']
								objeto_fecha_uefa=datetime.strptime(fecha_uefa,'%d %b %y')
								if objeto_fecha_uefa>fecha_mas_proxima and objeto_fecha_uefa<objeto_fecha:
									fecha_mas_proxima=objeto_fecha_uefa

					with open('calendario_copa_italia.csv') as csvfile:
						reader_copa = csv.DictReader(csvfile)
						for copa in reader_copa:
							if copa['copa_local']==local or copa['copa_visitante']==local:
								fecha_copa=copa['copa_fecha']
								objeto_fecha_copa=datetime.strptime(fecha_copa,'%d %b %y')
								if objeto_fecha_copa>fecha_mas_proxima and objeto_fecha_copa<objeto_fecha:
									fecha_mas_proxima=objeto_fecha_copa

					with open('partidos_serie_a.csv') as csvfile:
						reader_partidos = csv.DictReader(csvfile)
						for partidos in reader_partidos:
							if partidos['partidos_equipo_local']==local or partidos['partidos_equipo_visitante']==local:
								fecha_partidos=partidos['partidos_fecha']
								objeto_fecha_partidos=datetime.strptime(fecha_partidos,'%d %b %y')
								if objeto_fecha_partidos>fecha_mas_proxima and objeto_fecha_partidos<objeto_fecha:
									fecha_mas_proxima=objeto_fecha_partidos

				dias_descanso_local=abs(objeto_fecha-fecha_mas_proxima).days


				if jor==0:
					fecha_mas_proxima=objeto_fecha
				else:
					fecha_mas_proxima=datetime(2015,6,29)

					with open('calendario_champions.csv') as csvfile:
						reader_champions = csv.DictReader(csvfile)
						for champs in reader_champions:
							if champs['champions_local']==visitante or champs['champions_visitante']==visitante:
								fecha_champs=champs['champions_fecha']
								objeto_fecha_champions=datetime.strptime(fecha_champs,'%d %b %y')
								if objeto_fecha_champions>fecha_mas_proxima and objeto_fecha_champions<objeto_fecha:
									fecha_mas_proxima=objeto_fecha_champions

					with open('calendario_uefa.csv') as csvfile:
						reader_uefa = csv.DictReader(csvfile)
						for uefa in reader_uefa:
							if uefa['uefa_local']==visitante or uefa['uefa_visitante']==visitante:
								fecha_uefa=uefa['uefa_fecha']
								objeto_fecha_uefa=datetime.strptime(fecha_uefa,'%d %b %y')
								if objeto_fecha_uefa>fecha_mas_proxima and objeto_fecha_uefa<objeto_fecha:
									fecha_mas_proxima=objeto_fecha_uefa

					with open('calendario_copa_italia.csv') as csvfile:
						reader_copa = csv.DictReader(csvfile)
						for copa in reader_copa:
							if copa['copa_local']==visitante or copa['copa_visitante']==visitante:
								fecha_copa=copa['copa_fecha']
								objeto_fecha_copa=datetime.strptime(fecha_copa,'%d %b %y')
								if objeto_fecha_copa>fecha_mas_proxima and objeto_fecha_copa<objeto_fecha:
									fecha_mas_proxima=objeto_fecha_copa

					with open('partidos_serie_a.csv') as csvfile:
						reader_partidos = csv.DictReader(csvfile)
						for partidos in reader_partidos:
							if partidos['partidos_equipo_local']==visitante or partidos['partidos_equipo_visitante']==visitante:
								fecha_partidos=partidos['partidos_fecha']
								objeto_fecha_partidos=datetime.strptime(fecha_partidos,'%d %b %y')
								if objeto_fecha_partidos>fecha_mas_proxima and objeto_fecha_partidos<objeto_fecha:
									fecha_mas_proxima=objeto_fecha_partidos

				dias_descanso_visitante=abs(objeto_fecha-fecha_mas_proxima).days
				#print(temporada+" "+jornada+" "+local+" "+visitante+" "+resultado+" "+str(rivalidad))

				#ROTACION TITULARES LOCAL

				titular_jornada_actual=[]
				titular_jornada_pasada=[]
				suplente_jornada_actual=[]
				suplente_jornada_pasada=[]
				if temporada=="Temporada2020":
					with open('alineacion_seriea_2019_2020.csv') as csvfile:
						reader_alineacion = csv.DictReader(csvfile)
						for alineaciones in reader_alineacion:
							if alineaciones['Jornada']==jornada and alineaciones['Equipo']==local:
								if alineaciones['Estado']=='Titular':
									titular_jornada_actual.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_actual.append(alineaciones['Jugador'])
							if alineaciones['Jornada']==jornada_pasada and alineaciones['Equipo']==local:
								if alineaciones['Estado']=='Titular':
									titular_jornada_pasada.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_pasada.append(alineaciones['Jugador'])
				if temporada=="Temporada2019":
					with open('alineacion_seriea_2018_2019.csv') as csvfile:
						reader_alineacion = csv.DictReader(csvfile)
						for alineaciones in reader_alineacion:
							if alineaciones['Jornada']==jornada and alineaciones['Equipo']==local:
								if alineaciones['Estado']=='Titular':
									titular_jornada_actual.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_actual.append(alineaciones['Jugador'])
							if alineaciones['Jornada']==jornada_pasada and alineaciones['Equipo']==local:
								if alineaciones['Estado']=='Titular':
									titular_jornada_pasada.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_pasada.append(alineaciones['Jugador'])
				if temporada=="Temporada2018":
					with open('alineacion_seriea_2017_2018.csv') as csvfile:
						reader_alineacion = csv.DictReader(csvfile)
						for alineaciones in reader_alineacion:
							if alineaciones['Jornada']==jornada and alineaciones['Equipo']==local:
								if alineaciones['Estado']=='Titular':
									titular_jornada_actual.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_actual.append(alineaciones['Jugador'])
							if alineaciones['Jornada']==jornada_pasada and alineaciones['Equipo']==local:
								if alineaciones['Estado']=='Titular':
									titular_jornada_pasada.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_pasada.append(alineaciones['Jugador'])
				if temporada=="Temporada2017":
					with open('alineacion_seriea_2016_2017.csv') as csvfile:
						reader_alineacion = csv.DictReader(csvfile)
						for alineaciones in reader_alineacion:
							if alineaciones['Jornada']==jornada and alineaciones['Equipo']==local:
								if alineaciones['Estado']=='Titular':
									titular_jornada_actual.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_actual.append(alineaciones['Jugador'])
							if alineaciones['Jornada']==jornada_pasada and alineaciones['Equipo']==local:
								if alineaciones['Estado']=='Titular':
									titular_jornada_pasada.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_pasada.append(alineaciones['Jugador'])
				rotacion_titulares=0
				for titular_i in titular_jornada_actual:
					for titular_j in titular_jornada_pasada:
						if titular_i==titular_j:
							rotacion_titulares=rotacion_titulares+1

				rotacion_titulares_local=11-rotacion_titulares

				rotacion_suplentes=0
				for suplente_i in suplente_jornada_actual:
					for suplente_j in suplente_jornada_pasada:
						if suplente_i==suplente_j:
							rotacion_suplentes=rotacion_suplentes+1

				rotacion_suplentes_local=7-rotacion_suplentes

				if jor==0:
					rotacion_titulares_local=0
					rotacion_suplentes_local=0
					rotacion_titulares_visitante=0
					rotacion_suplentes_visitante=0

				if temporada=="Temporada2020":

					if jor>0:

						alineacion_actual_porteros=""
						alineacion_actual_defensas=[]
						alineacion_actual_medios=[]
						alineacion_actual_delanteros=[]

						for jugador_i in titular_jornada_actual:
							for jugador_j in plantilla_2019_2020:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_actual_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_actual_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_actual_medios.append(jugador_i)
									else:
										alineacion_actual_delanteros.append(jugador_i)

						alineacion_pasada_porteros=[]
						alineacion_pasada_defensas=[]
						alineacion_pasada_medios=[]
						alineacion_pasada_delanteros=[]

						for jugador_i in titular_jornada_pasada:
							for jugador_j in plantilla_2019_2020:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_pasada_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_pasada_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_pasada_medios.append(jugador_i)
									else:
										alineacion_pasada_delanteros.append(jugador_i)

						
						if alineacion_actual_porteros==alineacion_pasada_porteros:
							rotacion_porteros_local=0
						else:
							rotacion_porteros_local=1

						defensas_repetidos=0
						for defensas_1 in alineacion_actual_defensas:
							for defensas_2 in alineacion_pasada_defensas:
								if defensas_1==defensas_2:
									defensas_repetidos=defensas_repetidos+1

						max_defensas=0

						if len(alineacion_actual_defensas)>len(alineacion_pasada_defensas):
							max_defensas=len(alineacion_actual_defensas)
						else:
							max_defensas=len(alineacion_pasada_defensas)

						rotacion_defensas_local=abs(max_defensas-defensas_repetidos)

						medios_repetidos=0
						for medios_1 in alineacion_actual_medios:
							for medios_2 in alineacion_pasada_medios:
								if medios_1==medios_2:
									medios_repetidos=medios_repetidos+1

						max_medios=0

						if len(alineacion_actual_medios)>len(alineacion_pasada_medios):
							max_medios=len(alineacion_actual_medios)
						else:
							max_medios=len(alineacion_pasada_medios)

						rotacion_medios_local=abs(max_medios-medios_repetidos)


						delanteros_repetidos=0
						for delanteros_1 in alineacion_actual_delanteros:
							for delanteros_2 in alineacion_pasada_delanteros:
								if delanteros_1==delanteros_2:
									delanteros_repetidos=delanteros_repetidos+1

						max_delanteros=0

						if len(alineacion_actual_delanteros)>len(alineacion_pasada_delanteros):
							max_delanteros=len(alineacion_actual_delanteros)
						else:
							max_delanteros=len(alineacion_pasada_delanteros)

						rotacion_delanteros_local=abs(max_delanteros-delanteros_repetidos)



					else:

						rotacion_porteros_local=0
						rotacion_delanteros_local=0
						rotacion_medios_local=0
						rotacion_defensas_local=0
							
				if temporada=="Temporada2019":


					if jor>0:

						alineacion_actual_porteros=""
						alineacion_actual_defensas=[]
						alineacion_actual_medios=[]
						alineacion_actual_delanteros=[]

						for jugador_i in titular_jornada_actual:
							for jugador_j in plantilla_2018_2019:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_actual_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_actual_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_actual_medios.append(jugador_i)
									else:
										alineacion_actual_delanteros.append(jugador_i)

						alineacion_pasada_porteros=[]
						alineacion_pasada_defensas=[]
						alineacion_pasada_medios=[]
						alineacion_pasada_delanteros=[]

						for jugador_i in titular_jornada_pasada:
							for jugador_j in plantilla_2018_2019:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_pasada_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_pasada_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_pasada_medios.append(jugador_i)
									else:
										alineacion_pasada_delanteros.append(jugador_i)

						rotacion_porteros_local=0
						if alineacion_actual_porteros==alineacion_pasada_porteros:
							rotacion_porteros_local=0
						else:
							rotacion_porteros_local=1

						defensas_repetidos=0
						for defensas_1 in alineacion_actual_defensas:
							for defensas_2 in alineacion_pasada_defensas:
								if defensas_1==defensas_2:
									defensas_repetidos=defensas_repetidos+1

						max_defensas=0

						if len(alineacion_actual_defensas)>len(alineacion_pasada_defensas):
							max_defensas=len(alineacion_actual_defensas)
						else:
							max_defensas=len(alineacion_pasada_defensas)

						rotacion_defensas_local=abs(max_defensas-defensas_repetidos)

						medios_repetidos=0
						for medios_1 in alineacion_actual_medios:
							for medios_2 in alineacion_pasada_medios:
								if medios_1==medios_2:
									medios_repetidos=medios_repetidos+1

						max_medios=0

						if len(alineacion_actual_medios)>len(alineacion_pasada_medios):
							max_medios=len(alineacion_actual_medios)
						else:
							max_medios=len(alineacion_pasada_medios)

						rotacion_medios_local=abs(max_medios-medios_repetidos)


						delanteros_repetidos=0
						for delanteros_1 in alineacion_actual_delanteros:
							for delanteros_2 in alineacion_pasada_delanteros:
								if delanteros_1==delanteros_2:
									delanteros_repetidos=delanteros_repetidos+1

						max_delanteros=0

						if len(alineacion_actual_delanteros)>len(alineacion_pasada_delanteros):
							max_delanteros=len(alineacion_actual_delanteros)
						else:
							max_delanteros=len(alineacion_pasada_delanteros)

						rotacion_delanteros_local=abs(max_delanteros-delanteros_repetidos)



					else:

						rotacion_porteros_local=0
						rotacion_delanteros_local=0
						rotacion_medios_local=0
						rotacion_defensas_local=0
					
							
				if temporada=="Temporada2018":

					if jor>0:

						alineacion_actual_porteros=""
						alineacion_actual_defensas=[]
						alineacion_actual_medios=[]
						alineacion_actual_delanteros=[]

						for jugador_i in titular_jornada_actual:
							for jugador_j in plantilla_2017_2018:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_actual_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_actual_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_actual_medios.append(jugador_i)
									else:
										alineacion_actual_delanteros.append(jugador_i)

						alineacion_pasada_porteros=[]
						alineacion_pasada_defensas=[]
						alineacion_pasada_medios=[]
						alineacion_pasada_delanteros=[]

						for jugador_i in titular_jornada_pasada:
							for jugador_j in plantilla_2017_2018:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_pasada_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_pasada_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_pasada_medios.append(jugador_i)
									else:
										alineacion_pasada_delanteros.append(jugador_i)

						rotacion_porteros_local=0
						if alineacion_actual_porteros==alineacion_pasada_porteros:
							rotacion_porteros_local=0
						else:
							rotacion_porteros_local=1

						defensas_repetidos=0
						for defensas_1 in alineacion_actual_defensas:
							for defensas_2 in alineacion_pasada_defensas:
								if defensas_1==defensas_2:
									defensas_repetidos=defensas_repetidos+1

						max_defensas=0

						if len(alineacion_actual_defensas)>len(alineacion_pasada_defensas):
							max_defensas=len(alineacion_actual_defensas)
						else:
							max_defensas=len(alineacion_pasada_defensas)

						rotacion_defensas_local=abs(max_defensas-defensas_repetidos)

						medios_repetidos=0
						for medios_1 in alineacion_actual_medios:
							for medios_2 in alineacion_pasada_medios:
								if medios_1==medios_2:
									medios_repetidos=medios_repetidos+1

						max_medios=0

						if len(alineacion_actual_medios)>len(alineacion_pasada_medios):
							max_medios=len(alineacion_actual_medios)
						else:
							max_medios=len(alineacion_pasada_medios)

						rotacion_medios_local=abs(max_medios-medios_repetidos)


						delanteros_repetidos=0
						for delanteros_1 in alineacion_actual_delanteros:
							for delanteros_2 in alineacion_pasada_delanteros:
								if delanteros_1==delanteros_2:
									delanteros_repetidos=delanteros_repetidos+1

						max_delanteros=0

						if len(alineacion_actual_delanteros)>len(alineacion_pasada_delanteros):
							max_delanteros=len(alineacion_actual_delanteros)
						else:
							max_delanteros=len(alineacion_pasada_delanteros)

						rotacion_delanteros_local=abs(max_delanteros-delanteros_repetidos)



					else:

						rotacion_porteros_local=0
						rotacion_delanteros_local=0
						rotacion_medios_local=0
						rotacion_defensas_local=0
					
							
				if temporada=="Temporada2017":

					if jor>0:

						alineacion_actual_porteros=""
						alineacion_actual_defensas=[]
						alineacion_actual_medios=[]
						alineacion_actual_delanteros=[]

						for jugador_i in titular_jornada_actual:
							for jugador_j in plantilla_2016_2017:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_actual_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_actual_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_actual_medios.append(jugador_i)
									else:
										alineacion_actual_delanteros.append(jugador_i)

						alineacion_pasada_porteros=[]
						alineacion_pasada_defensas=[]
						alineacion_pasada_medios=[]
						alineacion_pasada_delanteros=[]

						for jugador_i in titular_jornada_pasada:
							for jugador_j in plantilla_2016_2017:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_pasada_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_pasada_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_pasada_medios.append(jugador_i)
									else:
										alineacion_pasada_delanteros.append(jugador_i)

						rotacion_porteros_local=0
						if alineacion_actual_porteros==alineacion_pasada_porteros:
							rotacion_porteros_local=0
						else:
							rotacion_porteros_local=1

						defensas_repetidos=0
						for defensas_1 in alineacion_actual_defensas:
							for defensas_2 in alineacion_pasada_defensas:
								if defensas_1==defensas_2:
									defensas_repetidos=defensas_repetidos+1

						max_defensas=0

						if len(alineacion_actual_defensas)>len(alineacion_pasada_defensas):
							max_defensas=len(alineacion_actual_defensas)
						else:
							max_defensas=len(alineacion_pasada_defensas)

						rotacion_defensas_local=abs(max_defensas-defensas_repetidos)

						medios_repetidos=0
						for medios_1 in alineacion_actual_medios:
							for medios_2 in alineacion_pasada_medios:
								if medios_1==medios_2:
									medios_repetidos=medios_repetidos+1

						max_medios=0

						if len(alineacion_actual_medios)>len(alineacion_pasada_medios):
							max_medios=len(alineacion_actual_medios)
						else:
							max_medios=len(alineacion_pasada_medios)

						rotacion_medios_local=abs(max_medios-medios_repetidos)


						delanteros_repetidos=0
						for delanteros_1 in alineacion_actual_delanteros:
							for delanteros_2 in alineacion_pasada_delanteros:
								if delanteros_1==delanteros_2:
									delanteros_repetidos=delanteros_repetidos+1

						max_delanteros=0

						if len(alineacion_actual_delanteros)>len(alineacion_pasada_delanteros):
							max_delanteros=len(alineacion_actual_delanteros)
						else:
							max_delanteros=len(alineacion_pasada_delanteros)

						rotacion_delanteros_local=abs(max_delanteros-delanteros_repetidos)



					else:

						rotacion_porteros_local=0
						rotacion_delanteros_local=0
						rotacion_medios_local=0
						rotacion_defensas_local=0
					
						
				#ROTACION TITULARES VISITANTE

				titular_jornada_actual=[]
				titular_jornada_pasada=[]
				suplente_jornada_actual=[]
				suplente_jornada_pasada=[]
				if temporada=="Temporada2020":
					with open('alineacion_seriea_2019_2020.csv') as csvfile:
						reader_alineacion = csv.DictReader(csvfile)
						for alineaciones in reader_alineacion:
							if alineaciones['Jornada']==jornada and alineaciones['Equipo']==visitante:
								if alineaciones['Estado']=='Titular':
									titular_jornada_actual.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_actual.append(alineaciones['Jugador'])
							if alineaciones['Jornada']==jornada_pasada and alineaciones['Equipo']==visitante:
								if alineaciones['Estado']=='Titular':
									titular_jornada_pasada.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_pasada.append(alineaciones['Jugador'])
				if temporada=="Temporada2019":
					with open('alineacion_seriea_2018_2019.csv') as csvfile:
						reader_alineacion = csv.DictReader(csvfile)
						for alineaciones in reader_alineacion:
							if alineaciones['Jornada']==jornada and alineaciones['Equipo']==visitante:
								if alineaciones['Estado']=='Titular':
									titular_jornada_actual.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_actual.append(alineaciones['Jugador'])
							if alineaciones['Jornada']==jornada_pasada and alineaciones['Equipo']==visitante:
								if alineaciones['Estado']=='Titular':
									titular_jornada_pasada.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_pasada.append(alineaciones['Jugador'])
				if temporada=="Temporada2018":
					with open('alineacion_seriea_2017_2018.csv') as csvfile:
						reader_alineacion = csv.DictReader(csvfile)
						for alineaciones in reader_alineacion:
							if alineaciones['Jornada']==jornada and alineaciones['Equipo']==visitante:
								if alineaciones['Estado']=='Titular':
									titular_jornada_actual.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_actual.append(alineaciones['Jugador'])
							if alineaciones['Jornada']==jornada_pasada and alineaciones['Equipo']==visitante:
								if alineaciones['Estado']=='Titular':
									titular_jornada_pasada.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_pasada.append(alineaciones['Jugador'])
				if temporada=="Temporada2017":
					with open('alineacion_seriea_2016_2017.csv') as csvfile:
						reader_alineacion = csv.DictReader(csvfile)
						for alineaciones in reader_alineacion:
							if alineaciones['Jornada']==jornada and alineaciones['Equipo']==visitante:
								if alineaciones['Estado']=='Titular':
									titular_jornada_actual.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_actual.append(alineaciones['Jugador'])
							if alineaciones['Jornada']==jornada_pasada and alineaciones['Equipo']==visitante:
								if alineaciones['Estado']=='Titular':
									titular_jornada_pasada.append(alineaciones['Jugador'])
								if alineaciones['Estado']=='Suplente':
									suplente_jornada_pasada.append(alineaciones['Jugador'])
				rotacion_titulares=0
				for titular_i in titular_jornada_actual:
					for titular_j in titular_jornada_pasada:
						if titular_i==titular_j:
							rotacion_titulares=rotacion_titulares+1

				rotacion_titulares_visitante=11-rotacion_titulares

				rotacion_suplentes=0
				for suplente_i in suplente_jornada_actual:
					for suplente_j in suplente_jornada_pasada:
						if suplente_i==suplente_j:
							rotacion_suplentes=rotacion_suplentes+1

				rotacion_suplentes_visitante=7-rotacion_suplentes

				if jor==0:
					rotacion_titulares_visitante=0
					rotacion_suplentes_visitante=0

				if temporada=="Temporada2020":

					if jor>0:

						alineacion_actual_porteros=""
						alineacion_actual_defensas=[]
						alineacion_actual_medios=[]
						alineacion_actual_delanteros=[]

						for jugador_i in titular_jornada_actual:
							for jugador_j in plantilla_2019_2020:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_actual_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_actual_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_actual_medios.append(jugador_i)
									else:
										alineacion_actual_delanteros.append(jugador_i)

						alineacion_pasada_porteros=[]
						alineacion_pasada_defensas=[]
						alineacion_pasada_medios=[]
						alineacion_pasada_delanteros=[]

						for jugador_i in titular_jornada_pasada:
							for jugador_j in plantilla_2019_2020:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_pasada_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_pasada_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_pasada_medios.append(jugador_i)
									else:
										alineacion_pasada_delanteros.append(jugador_i)

						
						if alineacion_actual_porteros==alineacion_pasada_porteros:
							rotacion_porteros_visitante=0
						else:
							rotacion_porteros_visitante=1

						defensas_repetidos=0
						for defensas_1 in alineacion_actual_defensas:
							for defensas_2 in alineacion_pasada_defensas:
								if defensas_1==defensas_2:
									defensas_repetidos=defensas_repetidos+1

						max_defensas=0

						if len(alineacion_actual_defensas)>len(alineacion_pasada_defensas):
							max_defensas=len(alineacion_actual_defensas)
						else:
							max_defensas=len(alineacion_pasada_defensas)

						rotacion_defensas_visitante=abs(max_defensas-defensas_repetidos)

						medios_repetidos=0
						for medios_1 in alineacion_actual_medios:
							for medios_2 in alineacion_pasada_medios:
								if medios_1==medios_2:
									medios_repetidos=medios_repetidos+1

						max_medios=0

						if len(alineacion_actual_medios)>len(alineacion_pasada_medios):
							max_medios=len(alineacion_actual_medios)
						else:
							max_medios=len(alineacion_pasada_medios)

						rotacion_medios_visitante=abs(max_medios-medios_repetidos)


						delanteros_repetidos=0
						for delanteros_1 in alineacion_actual_delanteros:
							for delanteros_2 in alineacion_pasada_delanteros:
								if delanteros_1==delanteros_2:
									delanteros_repetidos=abs(delanteros_repetidos+1)

						max_delanteros=0

						if len(alineacion_actual_delanteros)>len(alineacion_pasada_delanteros):
							max_delanteros=len(alineacion_actual_delanteros)
						else:
							max_delanteros=len(alineacion_pasada_delanteros)

						rotacion_delanteros_visitante=max_delanteros-delanteros_repetidos



					else:

						rotacion_porteros_visitante=0
						rotacion_delanteros_visitante=0
						rotacion_medios_visitante=0
						rotacion_defensas_visitante=0
							
				if temporada=="Temporada2019":


					if jor>0:

						alineacion_actual_porteros=""
						alineacion_actual_defensas=[]
						alineacion_actual_medios=[]
						alineacion_actual_delanteros=[]

						for jugador_i in titular_jornada_actual:
							for jugador_j in plantilla_2018_2019:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_actual_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_actual_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_actual_medios.append(jugador_i)
									else:
										alineacion_actual_delanteros.append(jugador_i)

						alineacion_pasada_porteros=[]
						alineacion_pasada_defensas=[]
						alineacion_pasada_medios=[]
						alineacion_pasada_delanteros=[]

						for jugador_i in titular_jornada_pasada:
							for jugador_j in plantilla_2018_2019:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_pasada_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_pasada_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_pasada_medios.append(jugador_i)
									else:
										alineacion_pasada_delanteros.append(jugador_i)

						rotacion_porteros_visitante=0
						if alineacion_actual_porteros==alineacion_pasada_porteros:
							rotacion_porteros_visitante=0
						else:
							rotacion_porteros_visitante=1

						defensas_repetidos=0
						for defensas_1 in alineacion_actual_defensas:
							for defensas_2 in alineacion_pasada_defensas:
								if defensas_1==defensas_2:
									defensas_repetidos=defensas_repetidos+1

						max_defensas=0

						if len(alineacion_actual_defensas)>len(alineacion_pasada_defensas):
							max_defensas=len(alineacion_actual_defensas)
						else:
							max_defensas=len(alineacion_pasada_defensas)

						rotacion_defensas_visitante=abs(max_defensas-defensas_repetidos)

						medios_repetidos=0
						for medios_1 in alineacion_actual_medios:
							for medios_2 in alineacion_pasada_medios:
								if medios_1==medios_2:
									medios_repetidos=medios_repetidos+1

						max_medios=0

						if len(alineacion_actual_medios)>len(alineacion_pasada_medios):
							max_medios=len(alineacion_actual_medios)
						else:
							max_medios=len(alineacion_pasada_medios)

						rotacion_medios_visitante=abs(max_medios-medios_repetidos)


						delanteros_repetidos=0
						for delanteros_1 in alineacion_actual_delanteros:
							for delanteros_2 in alineacion_pasada_delanteros:
								if delanteros_1==delanteros_2:
									delanteros_repetidos=delanteros_repetidos+1

						max_delanteros=0

						if len(alineacion_actual_delanteros)>len(alineacion_pasada_delanteros):
							max_delanteros=len(alineacion_actual_delanteros)
						else:
							max_delanteros=len(alineacion_pasada_delanteros)

						rotacion_delanteros_visitante=abs(max_delanteros-delanteros_repetidos)



					else:

						rotacion_porteros_visitante=0
						rotacion_delanteros_visitante=0
						rotacion_medios_visitante=0
						rotacion_defensas_visitante=0
					
							
				if temporada=="Temporada2018":

					if jor>0:

						alineacion_actual_porteros=""
						alineacion_actual_defensas=[]
						alineacion_actual_medios=[]
						alineacion_actual_delanteros=[]

						for jugador_i in titular_jornada_actual:
							for jugador_j in plantilla_2017_2018:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_actual_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_actual_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_actual_medios.append(jugador_i)
									else:
										alineacion_actual_delanteros.append(jugador_i)

						alineacion_pasada_porteros=[]
						alineacion_pasada_defensas=[]
						alineacion_pasada_medios=[]
						alineacion_pasada_delanteros=[]

						for jugador_i in titular_jornada_pasada:
							for jugador_j in plantilla_2017_2018:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_pasada_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_pasada_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_pasada_medios.append(jugador_i)
									else:
										alineacion_pasada_delanteros.append(jugador_i)

						rotacion_porteros_visitante=0
						if alineacion_actual_porteros==alineacion_pasada_porteros:
							rotacion_porteros_visitante=0
						else:
							rotacion_porteros_visitante=1

						defensas_repetidos=0
						for defensas_1 in alineacion_actual_defensas:
							for defensas_2 in alineacion_pasada_defensas:
								if defensas_1==defensas_2:
									defensas_repetidos=defensas_repetidos+1

						max_defensas=0

						if len(alineacion_actual_defensas)>len(alineacion_pasada_defensas):
							max_defensas=len(alineacion_actual_defensas)
						else:
							max_defensas=len(alineacion_pasada_defensas)

						rotacion_defensas_visitante=abs(max_defensas-defensas_repetidos)

						medios_repetidos=0
						for medios_1 in alineacion_actual_medios:
							for medios_2 in alineacion_pasada_medios:
								if medios_1==medios_2:
									medios_repetidos=medios_repetidos+1

						max_medios=0

						if len(alineacion_actual_medios)>len(alineacion_pasada_medios):
							max_medios=len(alineacion_actual_medios)
						else:
							max_medios=len(alineacion_pasada_medios)

						rotacion_medios_visitante=abs(max_medios-medios_repetidos)


						delanteros_repetidos=0
						for delanteros_1 in alineacion_actual_delanteros:
							for delanteros_2 in alineacion_pasada_delanteros:
								if delanteros_1==delanteros_2:
									delanteros_repetidos=delanteros_repetidos+1

						max_delanteros=0

						if len(alineacion_actual_delanteros)>len(alineacion_pasada_delanteros):
							max_delanteros=len(alineacion_actual_delanteros)
						else:
							max_delanteros=len(alineacion_pasada_delanteros)

						rotacion_delanteros_visitante=abs(max_delanteros-delanteros_repetidos)



					else:

						rotacion_porteros_visitante=0
						rotacion_delanteros_visitante=0
						rotacion_medios_visitante=0
						rotacion_defensas_visitante=0
					
							
				if temporada=="Temporada2017":

					if jor>0:

						alineacion_actual_porteros=""
						alineacion_actual_defensas=[]
						alineacion_actual_medios=[]
						alineacion_actual_delanteros=[]

						for jugador_i in titular_jornada_actual:
							for jugador_j in plantilla_2016_2017:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_actual_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_actual_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_actual_medios.append(jugador_i)
									else:
										alineacion_actual_delanteros.append(jugador_i)

						alineacion_pasada_porteros=[]
						alineacion_pasada_defensas=[]
						alineacion_pasada_medios=[]
						alineacion_pasada_delanteros=[]

						for jugador_i in titular_jornada_pasada:
							for jugador_j in plantilla_2016_2017:
								if jugador_i == jugador_j.nombre:
									if jugador_j.posicion=="Portero":
										alineacion_pasada_porteros=jugador_i
									elif jugador_j.posicion=="Defensa":
										alineacion_pasada_defensas.append(jugador_i)
									elif jugador_j.posicion=="Centrocampista":
										alineacion_pasada_medios.append(jugador_i)
									else:
										alineacion_pasada_delanteros.append(jugador_i)

						rotacion_porteros_visitante=0
						if alineacion_actual_porteros==alineacion_pasada_porteros:
							rotacion_porteros_visitante=0
						else:
							rotacion_porteros_visitante=1

						defensas_repetidos=0
						for defensas_1 in alineacion_actual_defensas:
							for defensas_2 in alineacion_pasada_defensas:
								if defensas_1==defensas_2:
									defensas_repetidos=defensas_repetidos+1

						max_defensas=0

						if len(alineacion_actual_defensas)>len(alineacion_pasada_defensas):
							max_defensas=len(alineacion_actual_defensas)
						else:
							max_defensas=len(alineacion_pasada_defensas)

						rotacion_defensas_visitante=abs(max_defensas-defensas_repetidos)

						medios_repetidos=0
						for medios_1 in alineacion_actual_medios:
							for medios_2 in alineacion_pasada_medios:
								if medios_1==medios_2:
									medios_repetidos=medios_repetidos+1

						max_medios=0

						if len(alineacion_actual_medios)>len(alineacion_pasada_medios):
							max_medios=len(alineacion_actual_medios)
						else:
							max_medios=len(alineacion_pasada_medios)

						rotacion_medios_visitante=abs(max_medios-medios_repetidos)


						delanteros_repetidos=0
						for delanteros_1 in alineacion_actual_delanteros:
							for delanteros_2 in alineacion_pasada_delanteros:
								if delanteros_1==delanteros_2:
									delanteros_repetidos=delanteros_repetidos+1

						max_delanteros=0

						if len(alineacion_actual_delanteros)>len(alineacion_pasada_delanteros):
							max_delanteros=len(alineacion_actual_delanteros)
						else:
							max_delanteros=len(alineacion_pasada_delanteros)

						rotacion_delanteros_visitante=abs(max_delanteros-delanteros_repetidos)



					else:

						rotacion_porteros_visitante=0
						rotacion_delanteros_visitante=0
						rotacion_medios_visitante=0
						rotacion_defensas_visitante=0
				writer.writerow([temporada,jornada,"LOCAL",local,visitante,resultado_local,rivalidad_local,rotacion_titulares_local,
					rotacion_suplentes_local,
					rotacion_porteros_local,rotacion_defensas_local,rotacion_medios_local,rotacion_delanteros_local, dias_descanso_local])
				writer.writerow([temporada,jornada,"VISITANTE",local,visitante,resultado_visitante,rivalidad_visitante,
					rotacion_titulares_visitante,
					rotacion_suplentes_visitante,
					rotacion_porteros_visitante,rotacion_defensas_visitante,rotacion_medios_visitante,rotacion_delanteros_visitante, 
					dias_descanso_visitante])
				#print(temporada+" "+jornada+" "+local+" "+visitante+" "+resultado+" "+str(rivalidad)+" "+str(rotacion_titulares)+
				#	" "+str(rotacion_suplentes)+" "+str(rotacion_porteros)+" "+str(rotacion_defensas)+" "+str(rotacion_medios)+
				#		" "+str(rotacion_delanteros))
						 
				

			
        