#!/bin/bash

echo "partidos liga santander"
python ./PARTIDOS/partidos.py
echo "partidos permier"
python ./PARTIDOS/partidos_premier.py
echo "partidos calcio"
python ./PARTIDOS/partidos_calcio.py
echo "partidos bundesliga"
python ./PARTIDOS/partidos_bundesliga.py

echo "clasificacion liga santander"
python ./CLASIFICACION-JORNADA/clasificacion_jornada.py
echo "clasificacion premier"
python ./CLASIFICACION-JORNADA/clasificacion_jornada_premier.py
echo "clasificacion calcio"
python ./CLASIFICACION-JORNADA/clasificacion_jornada_calcio.py
echo "clasificacion bundesliga"
python ./CLASIFICACION-JORNADA/clasificacion_jornada_bundesliga.py

echo "calendario champions"
python ./CHAMPIONS-COPA-UEFA/calendario-champions.py
echo "calendario uefa"
python ./CHAMPIONS-COPA-UEFA/calendario-europa.py
echo "calendario copa del rey"
python ./CHAMPIONS-COPA-UEFA/calendario-copa.py
echo "calendario carabao"
python ./CHAMPIONS-COPA-UEFA/calendario-carabao.py
echo "calendario fa cup"
python ./CHAMPIONS-COPA-UEFA/calendario-fa.py
echo "calendario copa italia"
python ./CHAMPIONS-COPA-UEFA/calendario-copa-italia.py
echo "calendario dfb pokal"
python ./CHAMPIONS-COPA-UEFA/calendario-dfb_pokal.py

echo "plantilla liga santander"
python ./PLANTILLA/plantilla.py
echo "plantilla premier"
python ./PLANTILLA/plantilla_premier.py 
echo "plantilla calcio"
python ./PLANTILLA/plantilla_seriea.py
echo "plantilla bundesliga"
python ./PLANTILLA/plantilla_bundesliga.py

echo "alineacion la liga 2020"
python ./ALINEACION/alineacion.py
echo "alineacion la liga 2019"
python ./ALINEACION/alineacion-2019.py
echo "alineacion la liga 2018"
python ./ALINEACION/alineacion-2018.py
echo "alineacion la liga 2017"
python ./ALINEACION/alineacion-2017.py
echo "alineacion permier"
python ./ALINEACION/alineacion_premier.py
echo "alineacion calcio"
python ./ALINEACION/alineacion_calcio.py
echo "alineacion bundesliga"
python ./ALINEACION/alineacion_bundesliga.py

