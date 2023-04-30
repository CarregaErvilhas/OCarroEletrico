#!/bin/bash

export SQLALCHEMY_SILENCE_UBER_WARNING=1

csvsql --db sqlite:///mobie.sqlite3 --create-if-not-exists --overwrite --insert MOBIe_Lista_de_postos.csv --table MOBIe_Lista_de_postos
csvsql --db sqlite:///mobie.sqlite3 --create-if-not-exists --overwrite --insert Porto.csv --table Porto

sqlite3 mobie.sqlite3 < views.sql
sqlite3 mobie.sqlite3 < views_porto.sql

sql2csv --db sqlite:///mobie.sqlite3 --query "select * from Todos_Os_Postos" > Todos_Os_Postos.csv
sql2csv --db sqlite:///mobie.sqlite3 --query "select * from Todos_CCS2_20_80_percent" > Todos_CCS2_20_80_percent.csv
sql2csv --db sqlite:///mobie.sqlite3 --query "select * from Todos_TYPE2_7kW_0_100_percent" > Todos_TYPE2_7kW_0_100_percent.csv
sql2csv --db sqlite:///mobie.sqlite3 --query "select * from Todos_TYPE2_22kW_0_100_percent" > Todos_TYPE2_22kW_0_100_percent.csv
sql2csv --db sqlite:///mobie.sqlite3 --query "select * from Porto_Todos_Os_Postos" > Porto_Todos_Os_Postos.csv
sql2csv --db sqlite:///mobie.sqlite3 --query "select * from Porto_CCS2_20_80_percent" > Porto_CCS2_20_80_percent.csv
sql2csv --db sqlite:///mobie.sqlite3 --query "select * from Porto_TYPE2_7kW_0_100_percent" > Porto_TYPE2_7kW_0_100_percent.csv
sql2csv --db sqlite:///mobie.sqlite3 --query "select * from Porto_TYPE2_22kW_0_100_percent" > Porto_TYPE2_22kW_0_100_percent.csv
