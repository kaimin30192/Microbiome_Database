#!/usr/bin/env python3
# Date : 2020/10/11
# Author : Kaimin
# description : This is a program to check reads numbers in the FastQ file of Raw data.

# List the files
import glob
import numpy as np
targetPattern_1 = r"*_1.fastq" 
files_1 = glob.glob(targetPattern_1)
reads_list_1 = list()
reads_length_1 = list()
# Load data by each
for filename_1 in files_1:
    print(filename_1)  
# Reads length counting
    count = 0
    for count, line in enumerate(open(filename_1, 'r')): 
        count += 1
        row = count % 4
        if row == 2 :
            line = line.strip('\n')
            reads_length_1.append(len(line))        
# Reads number counting
    reads = count // 4
    reads_list_1.append(reads)


targetPattern_2 = r"*_2.fastq" 
files_2 = glob.glob(targetPattern_2)
reads_list_2 = list()
reads_length_2 = list()
# Load data by each
for filename_2 in files_2:
    print(filename_2)  
# Reads length counting
    count = 0
    for count, line in enumerate(open(filename_2, 'r')): 
        count += 1
        row = count % 4
        if row == 2 :
            line = line.strip('\n')
            reads_length_2.append(len(line))        
# Reads number counting
    reads = count // 4
    reads_list_2.append(reads)
# Out put
data = open("Files_Statistic.txt","a")
print(">>> Raw reads (Pair end) <<<", file=data)
print("\033[1;36;1mSample reads number R1:\033[0m", np.average(reads_list_1), "\033[1;36;1m R2:\033[0m", np.average(reads_list_2)," \033[1;36;1mAverage of reads length R1:\033[0m", np.average(reads_length_1)," \033[1;36;1m R2:\033[0m", np.average(reads_length_2), " \033[1;36;1mStdev of reads length R1:\033[0m", np.std(reads_length_1, ddof=1), " \033[1;36;1mR2:\033[0m", np.std(reads_length_2, ddof=1), file=data)
data.close()