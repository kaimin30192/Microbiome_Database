#!/usr/bin/env python
# Date : 2021/07/31
# Author : Kaimin
# Description : This is a program to query data from Mysql database.
# Target samples file : Target.txt

from numpy.testing._private.utils import print_assert_equal
import pandas as pd
import numpy as np
import sqlalchemy
import re
import mysql.connector
from mysql.connector import Error
from pandas import DataFrame
pd.set_option('max_colwidth',100)

try:
    # 連接 MySQL 資料庫
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="kaimin",              
        password="atrixuan",
        database="metagenome")

    if connection.is_connected():
        # 顯示資料庫版本
        db_Info = connection.get_server_info()
        print("資料庫版本：", db_Info)

        # 顯示目前使用的資料庫
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("目前使用的資料庫：", record)

        # 查詢目標
        df = pd.DataFrame()
        Target_file = open("Target.txt","r")
        for line in iter(Target_file):
            Line = line.strip('\n')
            cursor = connection.cursor()
            query = "SELECT Run_id, Taxa, OTU FROM OTU_table WHERE Run_id='" + Line + "' AND NOT Taxa ='Unassigned';" 
            df_1 = pd.read_sql(query, connection)
            df = pd.concat([df_1,df])
        Result = df.groupby(['Run_id','Taxa'])['OTU'].sum().reset_index()
        # Output-Kingdom =============================================================================
        filter_K = Result['Taxa'].str.contains(pat = 'k__(\w)')
        Output_K = Result[filter_K].copy()
        Split_K = Output_K.copy()
        Split_K['Taxa_1'] = Split_K.Taxa.str.split(';')
        Split_K['Taxa_K'] = Split_K.Taxa_1.str.get(0)
        Split_K = Split_K.drop(columns = ['Taxa_1','Taxa'])
        Split_K['Taxa'] = Split_K['Taxa_K']
        Split_K = Split_K.drop(columns = ['Taxa_K'])
        Result_K = Split_K.groupby(['Run_id','Taxa'])['OTU'].sum().reset_index()
        File_K = Result_K.pivot(index='Taxa', columns='Run_id').fillna(0).astype(int)
        File_K.to_csv("Output_Table_Kingdom.tsv", sep='\t')
        # Output-Phylum =============================================================================
        filter_P = Output_K['Taxa'].str.contains(pat = 'p__(\w)')
        Output_P = Output_K[filter_P].copy()
        Split_P = Output_P.copy()
        Split_P['Taxa_1'] = Split_P.Taxa.str.split(';')
        Split_P['Taxa_K'] = Split_P.Taxa_1.str.get(0)
        Split_P['Taxa_P'] = Split_P.Taxa_1.str.get(1)
        Split_P = Split_P.drop(columns = ['Taxa_1','Taxa'])
        Split_P['Taxa'] = Split_P['Taxa_K'] + ',' + Split_P['Taxa_P']
        Split_P = Split_P.drop(columns = ['Taxa_K', 'Taxa_P'])
        Result_P = Split_P.groupby(['Run_id','Taxa'])['OTU'].sum().reset_index()
        File_P = Result_P.pivot(index='Taxa', columns='Run_id').fillna(0).astype(int)
        File_P.to_csv("Output_Table_Phylum.tsv", sep='\t')
        # Output-Class =============================================================================
        filter_C = Output_P['Taxa'].str.contains(pat = 'c__(\w)')
        Output_C = Output_P[filter_C].copy()
        Split_C = Output_C.copy()
        Split_C['Taxa_1'] = Split_C.Taxa.str.split(';')
        Split_C['Taxa_K'] = Split_C.Taxa_1.str.get(0)
        Split_C['Taxa_P'] = Split_C.Taxa_1.str.get(1)
        Split_C['Taxa_C'] = Split_C.Taxa_1.str.get(2)
        Split_C = Split_C.drop(columns = ['Taxa_1','Taxa'])
        Split_C['Taxa'] = Split_C['Taxa_K'] + ',' + Split_C['Taxa_P'] + ',' + Split_C['Taxa_C']
        Split_C = Split_C.drop(columns = ['Taxa_K', 'Taxa_P', 'Taxa_C'])
        Result_C = Split_C.groupby(['Run_id','Taxa'])['OTU'].sum().reset_index()
        File_C = Result_C.pivot(index='Taxa', columns='Run_id').fillna(0).astype(int)
        File_C.to_csv("Output_Table_Class.tsv", sep='\t')
        # Output-Order =============================================================================
        filter_O = Output_C['Taxa'].str.contains(pat = 'o__(\w)')
        Output_O = Output_C[filter_O].copy()
        Split_O = Output_O.copy()
        Split_O['Taxa_1'] = Split_O.Taxa.str.split(';')
        Split_O['Taxa_K'] = Split_O.Taxa_1.str.get(0)
        Split_O['Taxa_P'] = Split_O.Taxa_1.str.get(1)
        Split_O['Taxa_C'] = Split_O.Taxa_1.str.get(2)
        Split_O['Taxa_O'] = Split_O.Taxa_1.str.get(3)
        Split_O = Split_O.drop(columns = ['Taxa_1','Taxa'])
        Split_O['Taxa'] = Split_O['Taxa_K'] + ',' + Split_O['Taxa_P'] + ',' + Split_O['Taxa_C'] + ',' + Split_O['Taxa_O']
        Split_O = Split_O.drop(columns = ['Taxa_K', 'Taxa_P', 'Taxa_C', 'Taxa_O'])
        Result_O = Split_O.groupby(['Run_id','Taxa'])['OTU'].sum().reset_index()
        File_O = Result_O.pivot(index='Taxa', columns='Run_id').fillna(0).astype(int)
        File_O.to_csv("Output_Table_Order.tsv", sep='\t')
        # Output-Family =============================================================================
        filter_F = Output_O['Taxa'].str.contains(pat = 'f__(\w)')
        Output_F = Output_O[filter_F].copy()
        Split_F = Output_F.copy()
        Split_F['Taxa_1'] = Split_F.Taxa.str.split(';')
        Split_F['Taxa_K'] = Split_F.Taxa_1.str.get(0)
        Split_F['Taxa_P'] = Split_F.Taxa_1.str.get(1)
        Split_F['Taxa_C'] = Split_F.Taxa_1.str.get(2)
        Split_F['Taxa_O'] = Split_F.Taxa_1.str.get(3)
        Split_F['Taxa_F'] = Split_F.Taxa_1.str.get(4)
        Split_F = Split_F.drop(columns = ['Taxa_1','Taxa'])
        Split_F['Taxa'] = Split_F['Taxa_K'] + ',' + Split_F['Taxa_P'] + ',' + Split_F['Taxa_C'] + ',' + Split_F['Taxa_O'] + ',' + Split_F['Taxa_F']
        Split_F = Split_F.drop(columns = ['Taxa_K', 'Taxa_P', 'Taxa_C', 'Taxa_O', 'Taxa_F'])
        Result_F = Split_F.groupby(['Run_id','Taxa'])['OTU'].sum().reset_index()
        File_F = Result_F.pivot(index='Taxa', columns='Run_id').fillna(0).astype(int)
        File_F.to_csv("Output_Table_Family.tsv", sep='\t')
        # Output-Genus =============================================================================
        filter_G = Output_F['Taxa'].str.contains(pat = 'g__(\w)')
        Output_G = Output_F[filter_G].copy()
        Split_G = Output_G.copy()
        Split_G['Taxa_1'] = Split_G.Taxa.str.split(';')
        Split_G['Taxa_K'] = Split_G.Taxa_1.str.get(0)
        Split_G['Taxa_P'] = Split_G.Taxa_1.str.get(1)
        Split_G['Taxa_C'] = Split_G.Taxa_1.str.get(2)
        Split_G['Taxa_O'] = Split_G.Taxa_1.str.get(3)
        Split_G['Taxa_F'] = Split_G.Taxa_1.str.get(4)
        Split_G['Taxa_G'] = Split_G.Taxa_1.str.get(5)
        Split_G = Split_G.drop(columns = ['Taxa_1','Taxa'])
        Split_G['Taxa'] = Split_G['Taxa_K'] + ',' + Split_G['Taxa_P'] + ',' + Split_G['Taxa_C'] + ',' + Split_G['Taxa_O'] + ',' + Split_G['Taxa_F'] + ',' + Split_G['Taxa_G']
        Split_G = Split_G.drop(columns = ['Taxa_K', 'Taxa_P', 'Taxa_C', 'Taxa_O', 'Taxa_F', 'Taxa_G'])
        Result_G = Split_G.groupby(['Run_id','Taxa'])['OTU'].sum().reset_index()
        File_G = Result_G.pivot(index='Taxa', columns='Run_id').fillna(0).astype(int)
        File_G.to_csv("Output_Table_Genus.tsv", sep='\t')
        # Output-Species =============================================================================
        filter_S = Output_G['Taxa'].str.contains(pat = 's__(\w)')
        Output_S = Output_G[filter_S].copy()
        Split_S = Output_S.copy()
        Split_S['Taxa_1'] = Split_S.Taxa.str.split(';')
        Split_S['Taxa_K'] = Split_S.Taxa_1.str.get(0)
        Split_S['Taxa_P'] = Split_S.Taxa_1.str.get(1)
        Split_S['Taxa_C'] = Split_S.Taxa_1.str.get(2)
        Split_S['Taxa_O'] = Split_S.Taxa_1.str.get(3)
        Split_S['Taxa_F'] = Split_S.Taxa_1.str.get(4)
        Split_S['Taxa_G'] = Split_S.Taxa_1.str.get(5)
        Split_S['Taxa_S'] = Split_S.Taxa_1.str.get(6)
        Split_S = Split_S.drop(columns = ['Taxa_1','Taxa'])
        Split_S['Taxa'] = Split_S['Taxa_K'] + ',' + Split_S['Taxa_P'] + ',' + Split_S['Taxa_C'] + ',' + Split_S['Taxa_O'] + ',' + Split_S['Taxa_F'] + ',' + Split_S['Taxa_G'] + ',' + Split_S['Taxa_S']
        Split_S = Split_S.drop(columns = ['Taxa_K', 'Taxa_P', 'Taxa_C', 'Taxa_O', 'Taxa_F', 'Taxa_G', 'Taxa_S'])
        Result_S = Split_S.groupby(['Run_id','Taxa'])['OTU'].sum().reset_index()
        File_S = Result_S.pivot(index='Taxa', columns='Run_id').fillna(0).astype(int)
        File_S.to_csv("Output_Table_Species.tsv", sep='\t')
   
except Error as e:
    print("錯誤：", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("資料庫連線已關閉")    