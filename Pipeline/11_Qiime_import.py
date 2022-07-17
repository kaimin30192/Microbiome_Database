#!/usr/bin/env python
# Date : 2020/12/9
# Author : Kaimin
# Description : This is a program to pool chimera detected reads into Qiime2 import-file.

print(">>> Transform files to import formate ...")
import glob
targetPattern = r"NoChi_*" 
target_files = glob.glob(targetPattern)
if target_files :
    pool = open("Import.fna","a")
    for files in target_files :
        f = open(files,"r")
        lines = f.readlines()
        k = 1
        target_name = files.replace("NoChi_", "").replace(".fna", "")
        for line in lines :
            header_name = ">" + target_name + "_" + str(k) + " "
            s = line[:1]
            if s == ">" :
                k += 1
                line = line.strip('\n')
                new_header = line.replace(">",header_name)
                print(new_header, file = pool)
            else :
                line = line.strip('\n')
                print(line, file = pool)
    pool.close
    print(">>> done")