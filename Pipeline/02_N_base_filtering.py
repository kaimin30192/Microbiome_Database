#!/usr/bin/env python
# Date : 2020/11/23
# Author : Kaimin
# Description : This is a program to check N-base after seq trimming.

print(">>> N-base filtering ...")
import glob
import re

file_list = list()
# Targeting trimmed samples
targetPattern = r"Trimmed_*" 
files = glob.glob(targetPattern)
# N-base Filter
if files :
    for filename in files : 
        new_filename = filename.replace("Trimmed_","dN_")
        f1 = open(new_filename, "w")
        f2 = open(filename, "r")
        lines = f2.readlines()
        n = 0
        for line in lines :
            if n % 4 == 1 :
                if re.search("N", line) == None and re.search("n", line) == None :
                    f1.write(lines[(n-1)])
                    f1.write(lines[n])
                    f1.write(lines[(n+1)])
                    f1.write(lines[(n+2)])
            n += 1        
        f1.close
        f2.close            
print(">>> Done")                       