#!/usr/bin/env python
# Date : 2020/08/17
# Author : Kaimin
# Description : This is a program to convert .fastq files to .fasta files.

print(">>> Transform FastQ to FastA ...")
import os
import subprocess
from os import listdir
files = listdir("./")
if files :
    for filename in files : 
        if str("QtoA_") in filename :
            Output = filename.replace("QtoA_","PreProcessed_").replace(".fastq",".fasta")
            os.system("../../Tools/Qiime2_OTU_Pipeline/seqtk seq -a " + filename + " > " + Output)       
    print(">>> Done")
        