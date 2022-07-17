#!/bin/sh
# Date : 2020/11/26
# Author : Kaimin

ls | grep F_ > folder.txt

for Folder_name in $(cat folder.txt)
do 
	cd $Folder_name
	ls | grep .sra > List.txt
	for filename in $(cat List.txt)
	do 
		echo $filename
		fastq-dump $filename
	done
	rm List.txt
	rm *.sra
	cd ./..
done
rm folder.txt
exit