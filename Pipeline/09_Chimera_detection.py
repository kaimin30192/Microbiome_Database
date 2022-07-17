#!/usr/bin/env python
# Date : 2020/09/07
# Author : Kaimin
# Description : This is a program to check chimeric sequences.

print(">>> Do chimera detection ...")
import subprocess
import glob
#Chimera detect
targetPattern= r"Capi_PreProcessed_*"
files = glob.glob(targetPattern)
if files :
    for filename in files :  
        new_filename = filename.replace("Capi_PreProcessed_","Chimeras_")
        subprocess.call(['usearch', '-uchime2_ref', filename, '-db', '../../Tools/Qiime2_OTU_Pipeline/gold.fa', '-chimeras', new_filename, '-strand', 'plus', '-mode', 'sensitive', '-threads', '72'])      
    print(">>> Done")        



