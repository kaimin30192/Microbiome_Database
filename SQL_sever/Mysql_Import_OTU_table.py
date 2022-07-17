#!/usr/bin/env python
# Date : 2021/06/28
# Author : Kaimin
# Description : This is a program to import reference taxanomic data to Mysql database.

import re
import mysql.connector

mydb = mysql.connector.connect(
  host="140.120.202.182",
  user="kaimin",
  password="atrixuan",
  database="metagenome"
)
print(mydb)

f1 = open("OTU_table_reverse.tsv","r")
f2 = open("Run_id.txt","r")
f3 = open("OTU_taxa.tsv","r")
OTU_dictionary = {}
lines_1 = f1.readlines()
for item_1 in lines_1:
	item_1 = item_1.strip('\n')
	words = re.split('\s',item_1,2)
	key = words[0]
	key_val = words[-1]
	OTU_dictionary[key] = key_val
lines_2 = f2.read()
Run_id = lines_2.strip('\n')
lines_3 = f3.readlines()
for item_3 in lines_3:
	String = re.split('\t',item_3,2)
	Feature_id = String[0]
	Taxa = String[1]
	OTU_value = OTU_dictionary[Feature_id]
	mycursor = mydb.cursor()
	sql = "INSERT INTO OTU_table (Run_id, Feature_id, Taxa, OTU) VALUES (%s, %s, %s, %s)"
	val = (Run_id, Feature_id, Taxa, OTU_value)
	mycursor.execute(sql, val)
	mydb.commit()
f1.close()
f2.close()
f3.close()

mydb.close()

