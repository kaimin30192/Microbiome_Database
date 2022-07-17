#!/bin/bash
echo ">>> Do letters capitalize ..."
dir=$(ls -a ./ | grep "PreProcessed_" )
for sample in $dir
do 
  new_file_name=Capi_${sample}
  cat $sample | tr 'acgt' 'ACGT' > $new_file_name
done
echo ">>> Done"
exit