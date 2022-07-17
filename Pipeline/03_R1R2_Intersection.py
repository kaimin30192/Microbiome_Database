#!/usr/bin/env python
# Date : 2020/11/24
# Author : Kaimin
# Description : This is a program to match the R1,R2 reads after trimed.

print(">>> Finding R1 R2 intersection ...")
import os
from os.path import isfile, isdir, join
import subprocess
import re
# List the files 
filelist = os.listdir(os.getcwd())
dN_fastq_list = []
dN_R1 = []
dN_R2 = []
# Pick dN.fastq files in filelist
if filelist :
    for filename in filelist :
        if str("dN_") in filename : 
            dN_fastq_list.append(filename)
# Classify R1 R2 to each list[]
    if dN_fastq_list :
        for fastq_filename in dN_fastq_list :
            if str("_1") in fastq_filename :
                string1 = re.split('_1',fastq_filename)
                dN_R1.append(string1[-2])
            elif str("_2") in fastq_filename :
                string2 = re.split('_2',fastq_filename)
                dN_R2.append(string2[-2])
            else : 
                new_filename = fastq_filename.replace("dN_","QtoA_")
                subprocess.call(['mv', fastq_filename, new_filename])           
# Intersection of trim_R1 & trim_R2
            intersection_list = set(dN_R1).intersection(set(dN_R2))
# Load sequence into dictionary
        for keywords in intersection_list :
            if os.path.isfile(str(keywords)+'_1.fastq') == True :
                R1_filename = str(keywords)+'_1.fastq'   
            if os.path.isfile(str(keywords)+'_1_001.fastq') == True :
                R1_filename = str(keywords)+'_1_001.fastq' 
            if os.path.isfile(str(keywords)+'_2.fastq') == True :
                R2_filename = str(keywords)+'_2.fastq'
            if os.path.isfile(str(keywords)+'_2_001.fastq') == True :
                R2_filename = str(keywords)+'_2_001.fastq'
# Find R1 key & tail      
            dict_R1 = {}
            dict_R1_tail = {}
            dict_R2 = {}
            dict_R2_tail = {}
            key_R1 = 0
            value_R1 = []
            R1_tail = 0
            for count , line in enumerate(open(R1_filename,'r')):
                if count % 4 == 0 :
                    key_R1 = re.split('\s', line)[0] 
                    R1_tail = re.split('\s', line)[1]    
                if count % 4 == 1 :
                    value_R1.append(line)
                if count % 4 == 2 :
                    value_R1.append(line)
                if count % 4 == 3 :
                    value_R1.append(line)
                    dict_R1[key_R1] = value_R1
                    value_R1 = []
            open(R1_filename,'r').close
# Find R2 key & tail
            key_R2 = 0
            value_R2 = []
            R2_tail = 0
            for count , line in enumerate(open(R2_filename,'r')):
                if count % 4 == 0 :
                    key_R2 = re.split('\s', line)[0] 
                    R2_tail = re.split('\s', line)[1]
                if count % 4 == 1 :
                    value_R2.append(line)
                if count % 4 == 2 :
                    value_R2.append(line)
                if count % 4 == 3 :
                    value_R2.append(line)
                    dict_R2[key_R2] = value_R2
                    value_R2 = []
            open(R2_filename,'r').close
# Write in new R1
            new_R1 = {k:dict_R1[k] for k in dict_R1.keys() & dict_R2.keys()}
            file_R1 = open('Matched_'+str(R1_filename),'w')
            for key, value in new_R1.items() :
                file_R1.write(str(key)+'\n')
                for item in value :
                    file_R1.write(str(item))
            file_R1.close()
# Write in new R2
            new_R2 = {j:dict_R2[j] for j in dict_R1.keys() & dict_R2.keys()}
            file_R2 = open('Matched_'+str(R2_filename),'w')
            for key, value in new_R2.items() :
                file_R2.write(str(key)+'\n')
                for item in value :
                    file_R2.write(str(item))
            file_R2.close()
        print(">>> Done")
else :
    pass