#!/bin/bash
# Date : 2020/11/26
# Author : Kaimin

cd ../Single_End
Target=$(ls -a | grep '.fastq' | head -n 100)
for sample in $Target
do
	mv $sample ../Running_Pipeline/
done
exit