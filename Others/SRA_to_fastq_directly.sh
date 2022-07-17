#!/bin/sh
# Date : 2020/11/26
# Author : Kaimin

ls | grep .sra > List.txt
for filename in $(cat List.txt)
do 
	echo $filename
	fastq-dump $filename
done
rm List.txt
rm *.sra
exit