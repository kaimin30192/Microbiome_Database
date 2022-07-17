#!/usr/bin/env python
# Date : 2020/11/26
# Author : Kaimin
# Description : This is a program to Filter out samples which reads less than 50% after procress.

print(">>> 50 percents reads filtering ...")
import glob
import subprocess
# Find pair-end samples Before & After data processed
targetPattern_1= r"Matched_dN*"
After_files_1 = glob.glob(targetPattern_1)
if After_files_1 :
    for R1_files in After_files_1 :
        if str("_1") in R1_files :
            f1 = open(R1_files, "r")
            reads_number_f1 = len(f1.readlines())
            f1.close
            Raw_files_1 = R1_files.replace("Matched_dN_", "")
            f2 = open(Raw_files_1, "r")
            reads_number_f2 = len(f2.readlines())
            f2.close
            R2_files = R1_files.replace("_1", "_2")
            if reads_number_f2 < (reads_number_f1 / 2) :
                subprocess.call(['rm', R1_files, R2_files])
else :
    pass
targetPattern_2= r"QtoA_*"
After_files_2 = glob.glob(targetPattern_2)
if After_files_2 :
    for files in After_files_2 :
        h1 = open(files, "r")
        reads_number_h1 = len(h1.readlines())
        h1.close
        Raw_files_2 = files.replace("QtoA_", "")
        h2 = open(Raw_files_2, "r")
        reads_number_h2 = len(h2.readlines())
        h2.close
        if reads_number_h2 < int(reads_number_h1/2) :
            print("remove:", files)
            subprocess.call(['rm', files])
    print(">>> Done")
else :
    pass