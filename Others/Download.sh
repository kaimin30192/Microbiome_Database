#!/bin/bash
# Date : 2020/11/26
# Author : Kaimin

read -p "Please input Project number: " Project_number
mkdir ${Project_number}
for samplename in $(cat ${Project_number}_Acc_List.txt)
do
     fastq-dump --split-files -O ./${Project_number} ${samplename} &
done
exit