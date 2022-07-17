#!/usr/bin/env python
# Date : 2020/12/03
# Author : Kaimin
# Description : This is a program to make all letters capital.

print(">>> Do chimera sequences remove ...")
import re
import glob
targetPattern_1= r"Capi_PreProcessed_*"
files = glob.glob(targetPattern_1)
targetPattern_2= r"Chimeras_*"
Chimera_files = glob.glob(targetPattern_2)
if files :
    if Chimera_files :
        for file_name in files :
            f = open(file_name,"r")
            Chimera_file_name = file_name.replace("Capi_PreProcessed_","Chimeras_")
            h = open(Chimera_file_name,"r")
            dict = {}
            for line in iter(f):
                s = line[:1]
                if s == ">" :
                    value = []
                    key = line
                    value.clear
                else :
                    value.append(line)
                str=''
                dict[key] = str.join(value)
            for line in iter(h):
                s = line[:1]
                if s == ">" :
                    Chimera_key = line
                    del dict[Chimera_key]
            new_file_name = file_name.replace("Capi_PreProcessed_","NoChi_").replace(".fasta",".fna")
            output = open(new_file_name,"a")
            for item in dict.items() :
                output.writelines(item)
            output.close
        print(">>> Done")    
    

               