#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv  
import json  
  
# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ESTADISTICAS/goles_csv.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "Equipo", "Jornada", "Temporada", "Cambios_defensa_partido", "Cambio_lesion_partido", 
	"Titulares_cambio_jornadapasada", "exp_lambda", "y_lambda"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/ESTADISTICAS/goles_json.json', 'w')  
f.write(out)  
print "JSON saved!"  


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ESTADISTICAS/resultados_csv.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "Equipo", "Jornada", "Temporada", "Cambios_defensa_partido", "Cambio_jugador_lesion", 
	"Titulares_cambiados_jornada_anterior", "Puntos_y", "cut1_y", "cut2_y"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/ESTADISTICAS/resultados_json.json', 'w')  
f.write(out)  
print "JSON saved!"  


