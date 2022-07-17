#!/bin/bash
# Date : 2021/09/27
# Author : Kaimin
# Description : This is a program to merge OTU tables of multipule samples.

mkdir OTU_table_merge_tmp
Merge_order="qiime feature-table merge"
for Target_names in $(cat Target.txt)
do
    cd $Target_names
    File_name=$Target_names."qza"
    cp table-or-97.qza $File_name
    mv $File_name ../OTU_table_merge_tmp
    Merge_order="$Merge_order --i-tables $File_name"
    cd ./..
done
cd OTU_table_merge_tmp
Merge_order="$Merge_order --o-merged-table merged-table.qza"
$Merge_order
find . -maxdepth 1 ! -name merged-table.qza -exec rm -f {} \; 
qiime metadata tabulate --m-input-file merged-table.qza --o-visualization merged-table.qzv
cd ./..
exit
#qiime diversity alpha --i-table merged-table.qza --p-metric shannon --o-alpha-diversity Alpha_Output.qza --quiet
#qiime diversity beta --i-table table.qza --p-metric braycurtis --o-distance-matrix Beta_Output.qza --quiet
#qiime tools export --input-path Alpha_Output.qza --output-path ./
#qiime tools export table.qza --output-dir exported-feature-table
#qiime metadata tabulate --m-input-file Alpha_Output.qza --o-visualization Alpha_Output.qzv
#qiime diversity alpha-group-significance --i-alpha-diversity Alpha_Output.qza --m-metadata-file metadata_1.tsv --o-visualization Alpha_visual.qzv
#qiime tools export --input-path Alpha_Output.qza --output-path exported-feature-table --output-format BIOMV100Format
#qiime diversity alpha-rarefaction --i-table merged-table.qza --p-max-depth 19 --p-metrics shannon --o-visualization VISUALIZATION