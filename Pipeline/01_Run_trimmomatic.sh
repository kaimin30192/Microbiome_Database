#!/bin/sh
echo -e ">>> Quality Trimming ..."
java="/usr/bin/java"
trimmomatic_dir=/home/kaimin/software/Trimmomatic-0.39
dir=$(ls -a ./ | grep ".fastq" )
for sample in $dir
do
    fastq_file=$sample
    output=Trimmed_${sample}

    $java -jar $trimmomatic_dir/trimmomatic-0.39.jar \
        SE \
        -threads 72 \
        -phred33 \
        $fastq_file \
        $output \
        SLIDINGWINDOW:5:20         
done
echo ">>> Done"
exit
