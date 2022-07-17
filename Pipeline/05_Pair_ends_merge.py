#!/usr/bin/env python
# Date : 2020/08/10
# Author : Kaimin
# Description : This is a program to check N-base in R1,R2 reads.

print(">>> Mergeing pair-end samples ...")
import glob
import subprocess
# find target files
targetPattern= r"Matched_dN*_1*"
files = glob.glob(targetPattern)
if files :
    for target in files :
        R1_file = target 
        R2_file = target.replace("_1","_2")
        pair_file = target.replace("Matched_dN_","Merged_").replace("_1","")
        args = str("--output-prefix="+ pair_file)
        subprocess.call(['../../Tools/Qiime2_OTU_Pipeline/flash', '--max-mismatch-density=0.5', args, R1_file, R2_file])  
    print(">>> Done")                    