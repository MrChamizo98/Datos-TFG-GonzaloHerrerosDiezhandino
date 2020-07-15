#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv  
import json  
  
# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_premier_2019_2020.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_premier_2019_2020.json', 'w')  
f.write(out)  
print "JSON saved!"  


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_premier_2018_2019.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_premier_2018_2019.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_premier_2017_2018.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_premier_2017_2018.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_premier_2016_2017.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))    
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_premier_2016_2017.json', 'w')  
f.write(out)  
print "JSON saved!" 

###################################################################################################







#####################################################################################################

# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_bundesliga_2019_2020.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_bundesliga_2019_2020.json', 'w')  
f.write(out)  
print "JSON saved!"  


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_bundesliga_2018_2019.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_bundesliga_2018_2019.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_bundesliga_2017_2018.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_bundesliga_2017_2018.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_bundesliga_2016_2017.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_bundesliga_2016_2017.json', 'w')  
f.write(out)  
print "JSON saved!" 




################################################################################################








#################################################################################################

# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_seriea_2019_2020.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_seriea_2019_2020.json', 'w')  
f.write(out)  
print "JSON saved!"  


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_seriea_2018_2019.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_seriea_2018_2019.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_seriea_2017_2018.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_seriea_2017_2018.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_seriea_2016_2017.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))   
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_seriea_2016_2017.json', 'w')  
f.write(out)  
print "JSON saved!" 






###############################################################################################















###############################################################################################



# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_2019_2020.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))   
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_laliga_2019_2020.json', 'w')  
f.write(out)  
print "JSON saved!"  


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_2018_2019.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_laliga_2018_2019.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_2017_2018.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_laliga_2017_2018.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/ALINEACION/alineacion_2016_2017.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "alineacion_temporada",	"alineacion_jornada",	"alineacion_equipo",
	"alineacion_jugador",	"alineacion_estado",	"alineacion_cambio",	"alineacion_gol",	
	"alineacion_amarilla",	"alineacion_roja",	"alineacion_asistencia",	"alineacion_lesion"))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/alineacion_laliga_2016_2017.json', 'w')  
f.write(out)  
print "JSON saved!" 



