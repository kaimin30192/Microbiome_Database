#!/bin/bash
# Date : 2020/11/26
# Author : Kaimin
 
count=0
source_dir='./'
all_files=$(find $source_dir | grep '*.sra')  
 
mkdir F_01

 
for file in $files
do
    if expr $count % 3 == 0
    then
        mv -v $file ${target_dir1}
    elif expr $count % 3 == 1
    then
        mv -v $file ${target_dir2}
    else
        mv -v $file ${target_dir3}
    fi
    ((count++))
done
exit
