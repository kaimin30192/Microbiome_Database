#!/bin/bash
# Date : 2020/04/13
# Author : Kaimin
# Description : This program extract .tar.bz2 files at once commend.
# Target list : file_list.txt

for filename in $(cat file_list.txt)
do
	tar -xvzf ${filename}
done
exit 

