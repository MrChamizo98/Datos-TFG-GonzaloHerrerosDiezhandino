#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv  
import json  
  
# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_premier_2019_2020.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_premier_2019_2020.json', 'w')  
f.write(out)  
print "JSON saved!"  


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_premier_2018_2019.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_premier_2018_2019.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_premier_2017_2018.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_premier_2017_2018.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_premier_2016_2017.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_premier_2016_2017.json', 'w')  
f.write(out)  
print "JSON saved!" 

###################################################################################################







#####################################################################################################

# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_bundesliga_2019_2020.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_bundesliga_2019_2020.json', 'w')  
f.write(out)  
print "JSON saved!"  


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_bundesliga_2018_2019.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_bundesliga_2018_2019.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_bundesliga_2017_2018.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_bundesliga_2017_2018.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_bundesliga_2016_2017.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_bundesliga_2016_2017.json', 'w')  
f.write(out)  
print "JSON saved!" 




################################################################################################








#################################################################################################

# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_seriea_2019_2020.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_seriea_2019_2020.json', 'w')  
f.write(out)  
print "JSON saved!"  


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_seriea_2018_2019.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_seriea_2018_2019.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_seriea_2017_2018.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_seriea_2017_2018.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_seriea_2016_2017.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_seriea_2016_2017.json', 'w')  
f.write(out)  
print "JSON saved!" 






###############################################################################################















###############################################################################################



# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_españa_2019_2020.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_españa_2019_2020.json', 'w')  
f.write(out)  
print "JSON saved!"  


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_españa_2018_2019.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_españa_2018_2019.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_españa_2017_2018.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_españa_2017_2018.json', 'w')  
f.write(out)  
print "JSON saved!" 


# Open the CSV  
f = open('/home/gonzalo/Escritorio/TFG/PLANTILLA/plantilla_españa_2016_2017.csv','rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "plantilla_temporada",	"plantilla_equipo",
	"plantilla_dorsal",	"plantilla_foto",	"plantilla_name",	"plantilla_posicion",	"plantilla_edad",
		"plantilla_pais",	"plantilla_altura",	"plantilla_peso",	"plantilla_goles",	"plantilla_rojas",	"plantilla_amarillas"
))  
# Parse the CSV into JSON  
out = json.dumps( [row for row in reader] )  
print "JSON parsed!"  
# Save the JSON  
f = open( '/home/gonzalo/Escritorio/TFG/BD/plantilla_españa_2016_2017.json', 'w')  
f.write(out)  
print "JSON saved!" 



