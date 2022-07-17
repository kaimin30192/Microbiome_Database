#!/bin/bash
# Date : 2021/08/06
# Author : Kaimin
# Description : This is a program to run pipeline from Sequence-trim to OTU analysis.

# Move Target to Process Folder
find ./ -name "*.fastq" -type f > All_List.txt
for row in $(cat All_List.txt)
do  
    Target_Name=$(echo $row | cut -d "/" -f 2)
    # Pair-end reads ====================================================================
    if [[ $Target_Name =~ "_1." ]]
    then
        FolderName=${Target_Name%_1.*}
        printf "\E[0;36;40m"
        echo -e "\n\n>>> Processing sample $FolderName"
        printf "\E[0m"
        PairName=${Target_Name%_1.*}_2.fastq
        mkdir $FolderName
        cp $Target_Name $PairName ./$FolderName
        cd $FolderName
        # Statistic Raw Data
        python ../../Tools/Qiime2_OTU_Pipeline/Statistic_Pair_end_Raw_files.py
        # Quality Trimming
        sh ../../Tools/Qiime2_OTU_Pipeline/01_Run_trimmomatic.sh
        # Statistic Trimmed Data
        python ../../Tools/Qiime2_OTU_Pipeline/Statistic_Pair_end_Trimmed_files.py
        # N-base Filter
        python ../../Tools/Qiime2_OTU_Pipeline/02_N_base_filtering.py
        # Statistic N-filted Data
        python ../../Tools/Qiime2_OTU_Pipeline/Statistic_Pair_end_Nfilted_files.py
        # Connect Trimmed R1 & R2 Sequence
        python ../../Tools/Qiime2_OTU_Pipeline/03_R1R2_Intersection.py
        # Statistic Matched R1 R2 data
        python ../../Tools/Qiime2_OTU_Pipeline/Statistic_Matched_FastQ_files.py
        # Quality Filtering Sample Which Reads Less Than 50% After Processing
        python ../../Tools/Qiime2_OTU_Pipeline/04_Fifty_percent_quality_filtering.py
        # Merge R1 & R2 Sequence
        python ../../Tools/Qiime2_OTU_Pipeline/05_Pair_ends_merge.py
        # Statistic Merged data
        python ../../Tools/Qiime2_OTU_Pipeline/Statistic_Merged_FastQ_files.py
        # Remove
        rm *notCombined_1.fastq *notCombined_2.fastq *.histogram *.hist
        # Change ExtendedFrags File Name
        python ../../Tools/Qiime2_OTU_Pipeline/06_ExtendedFrags_files_rename.py
        # Transform FastQ to FastA
        python ../../Tools/Qiime2_OTU_Pipeline/07_Run_Seqtk.py
        # Make Letters in Sequence All Capital
        sh ../../Tools/Qiime2_OTU_Pipeline/08_Letters_capital.sh
        # Chimera Detection
        python ../../Tools/Qiime2_OTU_Pipeline/09_Chimera_detection.py
        # Remove Chimera Sequence
        python ../../Tools/Qiime2_OTU_Pipeline/10_Remove_Chimeras.py
        # Statistic Chimera Detected Data
        python ../../Tools/Qiime2_OTU_Pipeline/Statistic_Chimera_detected_files.py
        # Remove Processed Media File
        rm dN_* Matched_* QtoA_* Trimmed_* PreProcessed_* Capi_PreProcessed_* Chimeras_*
        # Change Qiime import formate
        python ../../Tools/Qiime2_OTU_Pipeline/11_Qiime_import.py
        # OTU clustering
        sh ../../Tools/Qiime2_OTU_Pipeline/12_Qiime2_OTU.sh
        # Remove Processed Media File
        rm Import.fna Import.qza rep-Import.qza table.qza
        # OTU table transform
        sh ../../Tools/Others/Qzv_to_csv.sh
        rm $Target_Name $PairName 
        cd ..
        echo $Target_Name >> ./Processed_files_log.txt
        echo $PairName >> ./Processed_files_log.txt
    elif [[ $Target_Name =~ "_2." ]]
    then
        :
    # Single-end reads ==================================================================   
    else
        FolderName=${Target_Name%.*}
        printf "\E[0;36;40m"
        echo -e "\n\n>>> Processing sample $FolderName"
        printf "\E[0m"
        mkdir $FolderName
        cp $Target_Name ./$FolderName
        cd $FolderName
        # Statistic Raw Data
        python ../../Tools/Qiime2_OTU_Pipeline/Statistic_Single_end_Raw_files.py
        # Quality Trimming
        sh ../../Tools/Qiime2_OTU_Pipeline/01_Run_trimmomatic.sh
        # Statistic Trimmed Data
        python ../../Tools/Qiime2_OTU_Pipeline/Statistic_Single_end_Trimmed_files.py
        # N-base Filter
        python ../../Tools/Qiime2_OTU_Pipeline/02_N_base_filtering.py
        # Statistic N-filted Data
        python ../../Tools/Qiime2_OTU_Pipeline/Statistic_Single_end_Nfilted_files.py
        # Connect Trimmed R1 & R2 Sequence (PASS)
        python ../../Tools/Qiime2_OTU_Pipeline/03_R1R2_Intersection.py
        # Quality Filtering Sample Which Reads Less Than 50% After Processing
        python ../../Tools/Qiime2_OTU_Pipeline/04_Fifty_percent_quality_filtering.py
        # Transform FastQ to FastA
        python ../../Tools/Qiime2_OTU_Pipeline/07_Run_Seqtk.py
        # Make Letters in Sequence All Capital
        sh ../../Tools/Qiime2_OTU_Pipeline/08_Letters_capital.sh
        # Chimera Detection
        python ../../Tools/Qiime2_OTU_Pipeline/09_Chimera_detection.py
        # Remove Chimera Sequence
        python ../../Tools/Qiime2_OTU_Pipeline/10_Remove_Chimeras.py
        # Statistic Chimera Detected Data
        python ../../Tools/Qiime2_OTU_Pipeline/Statistic_Chimera_detected_files.py
        # Remove Processed Media File
        rm QtoA_* Trimmed_* PreProcessed_* Capi_PreProcessed_* Chimeras_*
        # Change Qiime import formate
        python ../../Tools/Qiime2_OTU_Pipeline/11_Qiime_import.py
        # OTU clustering
        sh ../../Tools/Qiime2_OTU_Pipeline/12_Qiime2_OTU.sh
        # Remove Processed Media File
        rm Import.fna Import.qza rep-Import.qza table.qza
        # OTU table transform
        sh ../../Tools/Others/Qzv_to_csv.sh
        rm $Target_Name
        cd ..
        echo $Target_Name >> ./Processed_files_log.txt
    fi
done
rm All_List.txt
exit