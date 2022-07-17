#!/bin/bash
# Date : 2021/07/01
# Author : Kaimin
# Description : This program transform .qzv files to .csv files

cp table-or-97.qzv table-or-97.zip
cp taxonomy.qzv taxonomy.zip
unzip table-or-97.zip
dir=$(ls -l ./ |awk '/^d/ {print $NF}')
find ./$dir/data/ -name "metadata.tsv" -type f | xargs -i mv {} ./OTU_table.tsv
cat OTU_table.tsv | awk 'BEGIN{c=0;} {for(i=1;i<=NF;i++) {num[c,i] = $i;} c++;} END{ for(i=1;i<=NF;i++){str=""; for(j=0;j<NR;j++){ if(j>0){str = str" "} str= str""num[j,i]}printf("%s\n", str)} }' > Pre_OTU_table_reverse.tsv
sed '1d' Pre_OTU_table_reverse.tsv > OTU_table_reverse.tsv
find ./ -maxdepth 1 -name "*-*" -type d | xargs rm -r
unzip taxonomy.zip
dir2=$(ls -l ./ |awk '/^d/ {print $NF}')
find ./$dir2/data/ -name "metadata.tsv" -type f | xargs -i mv {} ./Pre_OTU_taxa.tsv
sed '1,2d' Pre_OTU_taxa.tsv > OTU_taxa.tsv
rm *.zip
rm new-*
rm Pre_*
find ./ -maxdepth 1 -name "*-*" -type d | xargs rm -r
exit

 
