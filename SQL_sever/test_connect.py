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
