#!/bin/sh
# Date : 2020/11/26
# Author : Kaimin

for filename in $(cat sff_list.txt)
do
    sff_extract $filename > ${filename%.*}.fastq
done
exit
