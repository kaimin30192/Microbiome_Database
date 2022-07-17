#!/usr/bin/env python3
# Date : 2020/10/11
# Author : Kaimin
# description : This is a program to check reads numbers in the FastQ file After Quality Trimming.

# Target the file
import glob
import numpy as np
targetPattern = r"Trimmed_*.fastq" 
files = glob.glob(targetPattern)
reads_list = list()
reads_length = list()
# Load data by each
for filename in files:
    print(filename)  
# Reads length counting
    count = 0
    for count, line in enumerate(open(filename, 'r')): 
        count += 1
        row = count % 4
        if row == 2 :
            line = line.strip('\n')
            reads_length.append(len(line))        
# Reads number counting
    reads = count // 4
    reads_list.append(reads)

# Out put
data = open("Files_Statistic.txt","a")
print(">>> After Quality Trimming <<<", file=data)
print("\033[1;36;1mSample reads number:\033[0m", np.average(reads_list), " \033[1;36;1mAverage of reads length:\033[0m", np.average(reads_length), " \033[1;36;1mStdev of reads length:\033[0m", np.std(reads_length, ddof=1), file=data)
data.close()