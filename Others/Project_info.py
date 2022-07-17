#!/usr/bin/env python
# Date : 2020/12/23
# Author : Kaimin
# Description : This is a program to get samples info of a project.

#----------------FastQ files--------------------
import glob
import numpy as np
targetPattern_A= r"*.fastq" 
files_A = glob.glob(targetPattern_A)
if files_A :
    len_A = len(files_A)
    reads_list_A = list()
    reads_length_A = list()
    pair = 0
    single = 0
    for filename_A in files_A:
        if str("_R1") in filename_A :
            pair += 1
        elif str("_R2") in filename_A :     
            pair += 1
        else :
            single += 1
#reads length counting
        count_A = 0
        for count_A, line_A in enumerate(open(filename_A, 'r')): 
            count_A += 1
            row = count_A % 4
            if row == 2 :
                line_A = line_A.strip('\n')
                reads_length_A.append(len(line_A))           
#reads number counting
        reads_A = count_A // 4
        reads_list_A.append(reads_A)
        num_A = count_A % 4
#out put
    data = open("Samples_FastQ_info.txt","a")
    print("Total FastQ files:\n", len_A, file=data)
    print("Average of reads number:\n", np.average(reads_list_A), file=data)
    print("Stdev of reads number:\n", np.std(reads_list_A), file=data)
    print("Average of reads length:\n", np.average(reads_length_A), file=data)
    print("Stdev of reads length:\n", np.std(reads_length_A), file=data)
    print("Single_end_FastQ:", single, file=data)
    print("Pair_end_FastQ:", pair, file=data)
    data.close()
else : 
    data = open("Samples_FastQ_info.txt","a")
    print("No FastQ files !", file=data)
    data.close()

#-----------------FastA files--------------------------
targetPattern_B= r"*.fasta" 
files_B = glob.glob(targetPattern_B)
if files_B :
    len_B = len(files_B)
    reads_list_B = list()
    reads_length_B = list()
    for filename_B in files_B:        
#reads length counting
        count_B = 0
        for count_B, line_B in enumerate(open(filename_B, 'r')): 
            count_B += 1
            row = count_B % 4
            if row == 2 :
                line_B = line_B.strip('\n')
                reads_length_B.append(len(line_B))           
#reads number counting
        reads_B = count_B // 2
        print ("Reads number:" , reads_B)
        reads_list_B.append(reads_B)
        num_B = count_B % 2
#out put
    data = open("Samples_info.txt","a")
    print("Total FastQ files:", len_A, file=data)
    print("Average of reads number:", np.average(reads_list_A), file=data)
    print("Stdev of reads number:", np.std(reads_list_A), file=data)
    print("Average of reads length:", np.average(reads_length_A), file=data)
    print("Stdev of reads length:", np.std(reads_length_A), file=data)
    data.close()
else :
    data = open("Files_Statistic.txt","a")
    print("AAAAAAA")
    data.close()