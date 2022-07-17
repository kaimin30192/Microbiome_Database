#!/usr/bin/env python
# Date : 2022/05/01
# Author : Kaimin
# Description : This is a program to get taxanomic data from each sample folder and merge as OTU table.

from re import split
from concurrent.futures import ProcessPoolExecutor
from pandas import DataFrame, concat
import warnings
warnings.filterwarnings("ignore", 'This pattern has match groups')


def poolA(sample):  # 依照list_of_Dataset_A.txt中的樣本開啟A.B兩個檔案，將A.B比對後的資料放入 *data_A = []
    Run_id = sample.strip('\n')
    with open("/home/DATA_32T/kaimin/Analysis/Samples_Data/" + Run_id + "/OTU_table_reverse.tsv", "r") as f1, open("/home/DATA_32T/kaimin/Analysis/Samples_Data/" + Run_id + "/OTU_taxa.tsv", "r") as f2:
        OTU_dictionary = {}
        for line in f1:
            line = line.strip("\n")
            words = split("\s", line, 2)
            OTU_dictionary[words[0]] = words[-1]
        All_row = []
        for line in f2:
            String = split('\t', line, 2)
            row = [Run_id + '_A', String[1], OTU_dictionary[String[0]]]
            All_row.append(row)
        All_row = list(filter(None, All_row))
    f1.close()
    f2.close()
    return All_row


def poolB(sample):  # 依照list_of_Dataset_A.txt中的樣本開啟A.B兩個檔案，將A.B比對後的資料放入 *data_A = []
    Run_id = sample.strip('\n')
    with open("/home/DATA_32T/kaimin/Analysis/Samples_Data/" + Run_id + "/OTU_table_reverse.tsv", "r") as f1, open("/home/DATA_32T/kaimin/Analysis/Samples_Data/" + Run_id + "/OTU_taxa.tsv", "r") as f2:
        OTU_dictionary = {}
        for line in f1:
            line = line.strip("\n")
            words = split("\s", line, 2)
            OTU_dictionary[words[0]] = words[-1]
        All_row = []
        for line in f2:
            String = split('\t', line, 2)
            row = [Run_id + '_B', String[1], OTU_dictionary[String[0]]]
            All_row.append(row)
        All_row = list(filter(None, All_row))
    f1.close()
    f2.close()
    return All_row


def getlistA(list_of_Dataset):
    with open(list_of_Dataset, "r") as listfile:  # ./Query_list/list_of_Dataset_A.txt
        sample = [f"{item}"for item in listfile]
        with ProcessPoolExecutor() as executor:
            test = executor.map(poolA, sample)
            see = list(test)
    data = []
    for sublist in see:
        for item in sublist:
            data.append(item)
    return data


def getlistB(list_of_Dataset):
    with open(list_of_Dataset, "r") as listfile:  # ./Query_list/list_of_Dataset_B.txt
        sample = [f"{item}"for item in listfile]
        with ProcessPoolExecutor() as executor:
            test = executor.map(poolB, sample)
            see = list(test)
    data = []
    for sublist in see:
        for item in sublist:
            data.append(item)
    return data


def analysis(data_input, Group):
    df = DataFrame(data_input, columns=['Run_id', 'Taxa', 'OTU'])
    df['OTU'] = df['OTU'].astype(int)
    df_filt = df[df["Taxa"] != "Unassigned"]
    Result = df_filt.groupby(['Run_id', 'Taxa'])[
        'OTU'].sum().reset_index()
    filter_K = Result['Taxa'].str.contains(pat='k__(\w)')  # Output-Kingdom
    Output_K = Result[filter_K].copy()
    filter_P = Output_K['Taxa'].str.contains(pat='p__(\w)')  # Output-Phylum
    Output_P = Output_K[filter_P].copy()
    filter_C = Output_P['Taxa'].str.contains(pat='c__(\w)')  # Output-Class
    Output_C = Output_P[filter_C].copy()
    filter_O = Output_C['Taxa'].str.contains(pat='o__(\w)')  # Output-Order
    Output_O = Output_C[filter_O].copy()
    filter_F = Output_O['Taxa'].str.contains(pat='f__(\w)')  # Output-Family
    Output_F = Output_O[filter_F].copy()
    filter_G = Output_F['Taxa'].str.contains(pat='g__(\w)')  # Output-Genus
    Output_G = Output_F[filter_G].copy()
    Split_G = Output_G.copy()
    Split_G['Taxa_1'] = Split_G.Taxa.str.split(';')
    Split_G['Taxa_K'] = Split_G.Taxa_1.str.get(0)
    Split_G['Taxa_P'] = Split_G.Taxa_1.str.get(1)
    Split_G['Taxa_C'] = Split_G.Taxa_1.str.get(2)
    Split_G['Taxa_O'] = Split_G.Taxa_1.str.get(3)
    Split_G['Taxa_F'] = Split_G.Taxa_1.str.get(4)
    Split_G['Taxa_G'] = Split_G.Taxa_1.str.get(5)
    Split_G = Split_G.drop(columns=['Taxa_1', 'Taxa'])
    Split_G['Taxa'] = Split_G['Taxa_K'] + ',' + Split_G['Taxa_P'] + ',' + Split_G['Taxa_C'] + \
        ',' + Split_G['Taxa_O'] + ',' + \
        Split_G['Taxa_F'] + ',' + Split_G['Taxa_G']
    Split_G = Split_G.drop(
        columns=['Taxa_K', 'Taxa_P', 'Taxa_C', 'Taxa_O', 'Taxa_F', 'Taxa_G'])
    Result_G = Split_G.groupby(['Run_id', 'Taxa'])[
        'OTU'].sum().reset_index()
    Result_G.columns = ['Run_id', 'Taxa', Group]
    File_G = Result_G.pivot(
        index='Taxa', columns='Run_id').fillna(0).astype(int)
    filter_S = Output_G['Taxa'].str.contains(pat='s__(\w)')  # Output-Species
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
    Split_S = Split_S.drop(columns=['Taxa_1', 'Taxa'])
    Split_S['Taxa'] = Split_S['Taxa_K'] + ',' + Split_S['Taxa_P'] + ',' + Split_S['Taxa_C'] + ',' + \
        Split_S['Taxa_O'] + ',' + Split_S['Taxa_F'] + ',' + \
        Split_S['Taxa_G'] + ',' + Split_S['Taxa_S']
    Split_S = Split_S.drop(
        columns=['Taxa_K', 'Taxa_P', 'Taxa_C', 'Taxa_O', 'Taxa_F', 'Taxa_G', 'Taxa_S'])
    Result_S = Split_S.groupby(['Run_id', 'Taxa'])[
        'OTU'].sum().reset_index()
    Result_S.columns = ['Run_id', 'Taxa', Group]
    File_S = Result_S.pivot(
        index='Taxa', columns='Run_id').fillna(0).astype(int)
    return [File_G, File_S]


def merge(File_G_Group_A, File_G_Group_B, File_S_Group_A, File_S_Group_B, tempfolder):
    # for Genus
    Merge_G_Group_AB = concat(
        [File_G_Group_A, File_G_Group_B], axis=1, join='outer').fillna(0).astype(int)
    Merge_G_Group_AB.to_csv(tempfolder + "G_A+B_pre.csv", sep='\t')
    Merge_G_Group_AB.to_csv(tempfolder + "G_Meta_pre.csv", sep='\t')
    df_G = Merge_G_Group_AB[:0]
    df_G_output = df_G.T
    df_G_output.to_csv(tempfolder + "G_preinfo.csv", sep='\t')

    # for Species
    Merge_S_Group_AB = concat(
        [File_S_Group_A, File_S_Group_B], axis=1, join='outer').fillna(0).astype(int)
    Merge_S_Group_AB.to_csv(tempfolder + "S_A+B_pre.csv", sep='\t')
    Merge_S_Group_AB.to_csv(tempfolder + "S_Meta_pre.csv", sep='\t')
    df_S = Merge_S_Group_AB[:0]
    df_S_output = df_S.T
    df_S_output.to_csv(tempfolder + "S_preinfo.csv", sep='\t')


def start(Dataset_A_list, Dataset_B_list, tempfolder):
    data_A = getlistA(Dataset_A_list)
    data_A_analyzed = analysis(data_A, 'Group_A')
    data_B = getlistB(Dataset_B_list)
    data_B_analyzed = analysis(data_B, 'Group_B')
    File_G_Group_A = data_A_analyzed[0]
    File_G_Group_B = data_B_analyzed[0]
    File_S_Group_A = data_A_analyzed[1]
    File_S_Group_B = data_B_analyzed[1]
    merge(File_G_Group_A, File_G_Group_B,
          File_S_Group_A, File_S_Group_B, tempfolder)
