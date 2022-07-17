#!/usr/bin/env python
# Date : 2020/08/20
# Author : Kaimin
# Description : This is a program to rename .extendedFrags .fastq file.

print(">>> Re-name merged files ...")
import os
import subprocess
from os import listdir
# rename
files = listdir("./")
for filename in files : 
    if str("Merged_") and str("extendedFrags") in filename :
        new_filename = filename.replace("Merged_","QtoA_").replace(".fastq.extendedFrags","")
        subprocess.call(['mv', filename, new_filename])
print(">>> Done")
