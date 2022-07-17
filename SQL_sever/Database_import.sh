#!/usr/bin/env python
# Date : 2022/02/24
# Author : Kaimin
# Description : This is a program to import datas with Mysql_import_OTU_table.py

find ./ -type d > folder.txt 
sed -i '1d' folder.txt
for Folder_name in $(cat folder.txt)
do 
	cd $Folder_name
    if [ -f "table-or-97.qza" ]; then
        echo $Folder_name | tr -d './' > Run_id.txt
        python ../../Tools/SQL_Sever/Mysql_Import_OTU_table.py
        echo $Folder_name
        rm Run_id.txt
        cd ./..
    else
        cd ./..
    fi
done
rm folder.txt
echo "All Finish"
exit
