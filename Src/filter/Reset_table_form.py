import pandas as pd
import fileinput
pd.set_option('max_colwidth', 100)


def Reset_form(tempfolder):

    # ============================ Genus ==============================================

    for line_k in fileinput.input(tempfolder + "G_preinfo.csv", inplace=1):
        if not fileinput.isfirstline():
            print(line_k.replace('\n', ''))
    df = pd.read_csv(tempfolder + 'G_preinfo.csv', header=None, sep='\t')
    df = df[[1, 0]]
    df.columns = ['X.SampleID', 'Dataset']
    df.insert(0, '', df['X.SampleID'])
    df.to_csv(tempfolder + "G_info.csv", sep=',')
    with open(tempfolder + 'G_Meta_pre.csv', 'r') as old_file_GM, open(tempfolder + 'G_Meta.csv', 'w+') as new_file_GM:
        data = old_file_GM.readlines()
        data_front = data[1:2]
        data_back = data[3:]
        new_file_GM.writelines(data_front)
        new_file_GM.writelines(data_back)
    new_file_GM.close
    df_G = pd.read_csv(tempfolder + "G_Meta.csv", delimiter="\t")
    df_assay_G = df_G.drop('Run_id', axis=1)
    df_assay_G.to_csv(tempfolder + "G_count.csv", sep='\t')
    df_rowData_G = df_G.loc[:, ['Run_id']]
    df_rowData_G['Run_id_split'] = df_rowData_G.Run_id.str.split(',')
    df_rowData_G['Kingdom'] = df_rowData_G.Run_id_split.str.get(0)
    df_rowData_G['Phylum'] = df_rowData_G.Run_id_split.str.get(1)
    df_rowData_G['Class'] = df_rowData_G.Run_id_split.str.get(2)
    df_rowData_G['Order'] = df_rowData_G.Run_id_split.str.get(3)
    df_rowData_G['Family'] = df_rowData_G.Run_id_split.str.get(4)
    df_rowData_G['Genus'] = df_rowData_G.Run_id_split.str.get(5)
    df_rowData_G = df_rowData_G.drop(columns=['Run_id_split', 'Run_id'])
    df_rowData_G.to_csv(tempfolder + "G_taxa.csv", sep='\t')
    with open(tempfolder + 'G_A+B_pre.csv', 'r') as old_file_G, open(tempfolder + 'G_A+B.csv', 'w') as new_file_G:
        data = old_file_G.readlines()
        data_1st = data[0:1]
        for i in data_1st:
            new_file_G.writelines('GROUP' + i)
        data_2st = data[1:2]
        new_file_G.writelines(data_2st)
        data_taxa = data[3:]
        for t in data_taxa:
            t = t.replace(', ', '|')
            new_file_G.writelines(t)
    new_file_G.close

# ============================ Species ==============================================

    for line_k in fileinput.input(tempfolder + "S_preinfo.csv", inplace=1):
        if not fileinput.isfirstline():
            print(line_k.replace('\n', ''))
    df = pd.read_csv(tempfolder + 'S_preinfo.csv', header=None, sep='\t')
    df = df[[1, 0]]
    df.columns = ['X.SampleID', 'Dataset']
    df.insert(0, '', df['X.SampleID'])
    df.to_csv(tempfolder + "S_info.csv", sep=',')
    with open(tempfolder + 'S_Meta_pre.csv', 'r') as old_file_SM, open(tempfolder + 'S_Meta.csv', 'w+') as new_file_SM:
        data = old_file_SM.readlines()
        data_front = data[1:2]
        data_back = data[3:]
        new_file_SM.writelines(data_front)
        new_file_SM.writelines(data_back)
    new_file_SM.close
    df_S = pd.read_csv(tempfolder + "S_Meta.csv", delimiter="\t")
    df_assay_S = df_S.drop('Run_id', axis=1)
    df_assay_S.to_csv(tempfolder + "S_count.csv", sep='\t')
    df_rowData_S = df_S.loc[:, ['Run_id']]
    df_rowData_S['Run_id_split'] = df_rowData_S.Run_id.str.split(',')
    df_rowData_S['Kingdom'] = df_rowData_S.Run_id_split.str.get(0)
    df_rowData_S['Phylum'] = df_rowData_S.Run_id_split.str.get(1)
    df_rowData_S['Class'] = df_rowData_S.Run_id_split.str.get(2)
    df_rowData_S['Order'] = df_rowData_S.Run_id_split.str.get(3)
    df_rowData_S['Family'] = df_rowData_S.Run_id_split.str.get(4)
    df_rowData_S['Genus'] = df_rowData_S.Run_id_split.str.get(5)
    df_rowData_S['Species'] = df_rowData_S.Run_id_split.str.get(6)
    df_rowData_S = df_rowData_S.drop(columns=['Run_id_split', 'Run_id'])
    df_rowData_S.to_csv(tempfolder + "S_taxa.csv", sep='\t')
    with open(tempfolder + 'S_A+B_pre.csv', 'r') as old_file_S, open(tempfolder + 'S_A+B.csv', 'w+') as new_file_S:
        data = old_file_S.readlines()
        data_1st = data[0:1]
        for i in data_1st:
            new_file_S.writelines('GROUP' + i)
        data_2st = data[1:2]
        new_file_S.writelines(data_2st)
        data_taxa = data[3:]
        for t in data_taxa:
            t = t.replace(', ', '|')
            new_file_S.writelines(t)
    new_file_S.close
