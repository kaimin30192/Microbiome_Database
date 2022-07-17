import os
import shutil
from djpjax import pjax
from pdf2image import convert_from_path
from time import process_time
from django.shortcuts import render
from django.http import JsonResponse
from django.template.response import TemplateResponse
from .models import Metadatatable, Phenotypetable
from .merge_OTU_table import start
from .Reset_table_form import Reset_form
from django.db import connection
cursor = connection.cursor()

# Create your views here.


@pjax()
def home_view(request):
    return TemplateResponse(request, 'home.html', {'text': 'Hello world x2'})


@pjax()
def analysis_view(request):
    alltype = Phenotypetable.objects.values('phenotype').distinct()
    return TemplateResponse(request, 'filter/analysis.html', {'alltype': alltype})


@pjax()
def data_view(request):
    return TemplateResponse(request, 'data.html', {'text': 'Hello world x2'})


def phenotype_01_select_view(request):
    if request.is_ajax():
        if request.method == "POST":
            phenotype_1 = request.POST['phenotype1']
            try:
                phenotype_Result_1_for_gender = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable WHERE phenotype = %s ) GROUP BY Sex", [phenotype_1])
                result_1_for_gender = []
                for obj_1 in phenotype_Result_1_for_gender:
                    if obj_1.sex != "":
                        item_1 = {
                            'sex': obj_1.sex,
                        }
                        result_1_for_gender.append(item_1)
                phenotype_Result_1_for_geo = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable WHERE phenotype = %s ) GROUP BY GeoLocation", [phenotype_1])
                result_1_for_geo = []
                for obj_1 in phenotype_Result_1_for_geo:
                    if obj_1.geolocation != "":
                        item_1 = {
                            'geo_location': obj_1.geolocation,
                        }
                        result_1_for_geo.append(item_1)
            except Exception:
                print("error")
            return JsonResponse({'result_1_for_gender': result_1_for_gender, 'result_1_for_geo': result_1_for_geo})


def phenotype_02_select_view(request):
    if request.is_ajax():
        if request.method == "POST":
            phenotype_2 = request.POST['phenotype2']
            try:
                phenotype_Result_2_for_gender = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable WHERE phenotype = %s ) GROUP BY Sex", [phenotype_2])
                result_2_for_gender = []
                for obj_2 in phenotype_Result_2_for_gender:
                    if obj_2.sex != "":
                        item_2 = {
                            'sex': obj_2.sex,
                        }
                        result_2_for_gender.append(item_2)
                phenotype_Result_2_for_geo = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable WHERE phenotype = %s ) GROUP BY GeoLocation", [phenotype_2])
                result_2_for_geo = []
                for obj_2 in phenotype_Result_2_for_geo:
                    if obj_2.geolocation != "":
                        item_2 = {
                            'geo_location': obj_2.geolocation,
                        }
                        result_2_for_geo.append(item_2)
            except Exception:
                print("error")
            return JsonResponse({'result_2_for_gender': result_2_for_gender, 'result_2_for_geo': result_2_for_geo})


def gender_01_select_view(request):
    if request.is_ajax():
        if request.method == "POST":
            gender_1 = request.POST['gender1']
            phenotype_1 = request.POST['phenotype1']
            try:
                gender_Result_1 = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable WHERE phenotype = %s ) AND Sex = %s GROUP BY GeoLocation", [phenotype_1, gender_1])
                result_3 = []
                for obj_3 in gender_Result_1:
                    if obj_3.geolocation != "":
                        item_3 = {
                            'geo_location': obj_3.geolocation,
                        }
                        result_3.append(item_3)
                print(result_3)
            except Exception:
                print("error")
            return JsonResponse({'result_3': result_3})


def gender_02_select_view(request):
    if request.is_ajax():
        if request.method == "POST":
            gender_2 = request.POST['gender2']
            phenotype_2 = request.POST['phenotype2']
            try:
                gender_Result_2 = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable WHERE phenotype = %s ) AND Sex = %s GROUP BY GeoLocation", [phenotype_2, gender_2])
                result_4 = []
                for obj_4 in gender_Result_2:
                    if obj_4.geolocation != "":
                        item_4 = {
                            'geo_location': obj_4.geolocation,
                        }
                        result_4.append(item_4)
            except Exception:
                print("error")
            return JsonResponse({'result_4': result_4})


def submit_1_view(request):
    if request.is_ajax():
        phenotype_1 = request.POST['phenotype1']
        gender_1 = request.POST['gender1']
        geo_1 = request.POST['geo1']
        age_1_bottom = request.POST['age1Bottom'] if request.POST['age1Bottom'] != "" else 0
        age_1_top = request.POST['age1Top'] if request.POST['age1Top'] != "" else 99
        bmi_1_bottom = request.POST['bmi1Bottom'] if request.POST['bmi1Bottom'] != "" else 0
        bmi_1_top = request.POST['bmi1Top'] if request.POST['bmi1Top'] != "" else 60
        if gender_1 != "Not specify" and geo_1 != "Not specify":
            final_1A = Metadatatable.objects.raw(
                "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Sex = %s AND GeoLocation = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_1, gender_1, geo_1, age_1_bottom, age_1_top, bmi_1_bottom, bmi_1_top])
            list_final = []
            for objA in final_1A:
                item_A = {
                    'run': objA.run,
                    'sex': objA.sex,
                    'age': objA.age,
                    'bmi': objA.bmi,
                    'geo_location': objA.geolocation,
                    'librarylayout': objA.librarylayout,
                    'platform': objA.platform,
                    'model': objA.model,
                    'srastudy': objA.srastudy,
                    'bioproject': objA.bioproject,
                    'biosample': objA.biosample,
                }
                list_final.append(item_A)
        if gender_1 == "Not specify" and geo_1 != "Not specify":
            final_1A = Metadatatable.objects.raw(
                "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND GeoLocation = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_1, geo_1, age_1_bottom, age_1_top, bmi_1_bottom, bmi_1_top])
            list_final = []
            for objA in final_1A:
                item_A = {
                    'run': objA.run,
                    'sex': objA.sex,
                    'age': objA.age,
                    'bmi': objA.bmi,
                    'geo_location': objA.geolocation,
                    'librarylayout': objA.librarylayout,
                    'platform': objA.platform,
                    'model': objA.model,
                    'srastudy': objA.srastudy,
                    'bioproject': objA.bioproject,
                    'biosample': objA.biosample,
                }
                list_final.append(item_A)
        if gender_1 != "Not specify" and geo_1 == "Not specify":
            final_1A = Metadatatable.objects.raw(
                "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Sex = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_1, gender_1, age_1_bottom, age_1_top, bmi_1_bottom, bmi_1_top])
            list_final = []
            for objA in final_1A:
                item_A = {
                    'run': objA.run,
                    'sex': objA.sex,
                    'age': objA.age,
                    'bmi': objA.bmi,
                    'geo_location': objA.geolocation,
                    'librarylayout': objA.librarylayout,
                    'platform': objA.platform,
                    'model': objA.model,
                    'srastudy': objA.srastudy,
                    'bioproject': objA.bioproject,
                    'biosample': objA.biosample,
                }
                list_final.append(item_A)
        if gender_1 == "Not specify" and geo_1 == "Not specify":
            final_1A = Metadatatable.objects.raw(
                "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_1, age_1_bottom, age_1_top, bmi_1_bottom, bmi_1_top])
            list_final = []
            for objA in final_1A:
                item_A = {
                    'run': objA.run,
                    'sex': objA.sex,
                    'age': objA.age,
                    'bmi': objA.bmi,
                    'geo_location': objA.geolocation,
                    'librarylayout': objA.librarylayout,
                    'platform': objA.platform,
                    'model': objA.model,
                    'srastudy': objA.srastudy,
                    'bioproject': objA.bioproject,
                    'biosample': objA.biosample,
                }
                list_final.append(item_A)
        return JsonResponse({'list_final': list_final})


def submit_2_view(request):
    if request.is_ajax():
        phenotype_2 = request.POST['phenotype2']
        gender_2 = request.POST['gender2']
        geo_2 = request.POST['geo2']
        age_2_bottom = request.POST['age2Bottom'] if request.POST['age2Bottom'] != "" else 0
        age_2_top = request.POST['age2Top'] if request.POST['age2Top'] != "" else 99
        bmi_2_bottom = request.POST['bmi2Bottom'] if request.POST['bmi2Bottom'] != "" else 0
        bmi_2_top = request.POST['bmi2Top'] if request.POST['bmi2Top'] != "" else 60
        if gender_2 != "Not specify" and geo_2 != "Not specify":
            final_2A = Metadatatable.objects.raw(
                "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Sex = %s AND GeoLocation = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_2, gender_2, geo_2, age_2_bottom, age_2_top, bmi_2_bottom, bmi_2_top])
            list_final = []
            for objA in final_2A:
                item_A = {
                    'run': objA.run,
                    'sex': objA.sex,
                    'age': objA.age,
                    'bmi': objA.bmi,
                    'geo_location': objA.geolocation,
                    'librarylayout': objA.librarylayout,
                    'platform': objA.platform,
                    'model': objA.model,
                    'srastudy': objA.srastudy,
                    'bioproject': objA.bioproject,
                    'biosample': objA.biosample,
                }
                list_final.append(item_A)
        if gender_2 == "Not specify" and geo_2 != "Not specify":
            final_2A = Metadatatable.objects.raw(
                "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND GeoLocation = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_2, geo_2, age_2_bottom, age_2_top, bmi_2_bottom, bmi_2_top])
            list_final = []
            for objA in final_2A:
                item_A = {
                    'run': objA.run,
                    'sex': objA.sex,
                    'age': objA.age,
                    'bmi': objA.bmi,
                    'geo_location': objA.geolocation,
                    'librarylayout': objA.librarylayout,
                    'platform': objA.platform,
                    'model': objA.model,
                    'srastudy': objA.srastudy,
                    'bioproject': objA.bioproject,
                    'biosample': objA.biosample,
                }
                list_final.append(item_A)
        if gender_2 != "Not specify" and geo_2 == "Not specify":
            final_2A = Metadatatable.objects.raw(
                "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Sex = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_2, gender_2, age_2_bottom, age_2_top, bmi_2_bottom, bmi_2_top])
            list_final = []
            for objA in final_2A:
                item_A = {
                    'run': objA.run,
                    'sex': objA.sex,
                    'age': objA.age,
                    'bmi': objA.bmi,
                    'geo_location': objA.geolocation,
                    'librarylayout': objA.librarylayout,
                    'platform': objA.platform,
                    'model': objA.model,
                    'srastudy': objA.srastudy,
                    'bioproject': objA.bioproject,
                    'biosample': objA.biosample,
                }
                list_final.append(item_A)
        if gender_2 == "Not specify" and geo_2 == "Not specify":
            final_2A = Metadatatable.objects.raw(
                "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_2, age_2_bottom, age_2_top, bmi_2_bottom, bmi_2_top])
            list_final = []
            for objA in final_2A:
                item_A = {
                    'run': objA.run,
                    'sex': objA.sex,
                    'age': objA.age,
                    'bmi': objA.bmi,
                    'geo_location': objA.geolocation,
                    'librarylayout': objA.librarylayout,
                    'platform': objA.platform,
                    'model': objA.model,
                    'srastudy': objA.srastudy,
                    'bioproject': objA.bioproject,
                    'biosample': objA.biosample,
                }
                list_final.append(item_A)
        return JsonResponse({'list_final': list_final})


def start_analysis_view(request):
    if request.is_ajax():
        time_stemp = process_time()
        phenotype_1 = request.POST['phenotype1']
        gender_1 = request.POST['gender1']
        geo_1 = request.POST['geo1']
        age_1_bottom = request.POST['age1Bottom'] if request.POST['age1Bottom'] != "" else 0
        age_1_top = request.POST['age1Top'] if request.POST['age1Top'] != "" else 99
        bmi_1_bottom = request.POST['bmi1Bottom'] if request.POST['bmi1Bottom'] != "" else 0
        bmi_1_top = request.POST['bmi1Top'] if request.POST['bmi1Top'] != "" else 60
        phenotype_2 = request.POST['phenotype2']
        gender_2 = request.POST['gender2']
        geo_2 = request.POST['geo2']
        age_2_bottom = request.POST['age2Bottom'] if request.POST['age2Bottom'] != "" else 0
        age_2_top = request.POST['age2Top'] if request.POST['age2Top'] != "" else 99
        bmi_2_bottom = request.POST['bmi2Bottom'] if request.POST['bmi2Bottom'] != "" else 0
        bmi_2_top = request.POST['bmi2Top'] if request.POST['bmi2Top'] != "" else 60

    # ===================================================== File path setting ===================================================================================================

        folderpath = "./media/" + phenotype_1 + "_" + gender_1 + "_" + geo_1 + "_" + str(age_1_bottom) + "-" + str(age_1_top) + "_" + str(bmi_1_bottom) + "-" + \
            str(bmi_1_top) + "_" + phenotype_2 + "_" + gender_2 + "_" + geo_2 + "_" + \
            str(age_2_bottom) + "-" + str(age_2_top) + "_" + \
            str(bmi_2_bottom) + "-" + str(bmi_2_top) + "/"
        folderpath_2 = "/media/" + phenotype_1 + "_" + gender_1 + "_" + geo_1 + "_" + str(age_1_bottom) + "-" + str(age_1_top) + "_" + str(bmi_1_bottom) + "-" + \
            str(bmi_1_top) + "_" + phenotype_2 + "_" + gender_2 + "_" + geo_2 + "_" + \
            str(age_2_bottom) + "-" + str(age_2_top) + "_" + \
            str(bmi_2_bottom) + "-" + str(bmi_2_top) + "/"
        if os.path.isdir(folderpath):
            return JsonResponse({'folderpath': folderpath_2})
        else:
            os.mkdir(folderpath)
            tempfolder = './Temp/' + \
                str(time_stemp) + '/'
            os.mkdir(tempfolder)
            list_A_path = './Temp/' + \
                str(time_stemp) + '/list_of_Dataset_A.txt'
            list_B_path = './Temp/' + \
                str(time_stemp) + '/list_of_Dataset_B.txt'

            # ======================================================================== Group A ==============================================================================================================

            if gender_1 != "Not specify" and geo_1 != "Not specify":
                final_1A = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Sex = %s AND GeoLocation = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_1, gender_1, geo_1, age_1_bottom, age_1_top, bmi_1_bottom, bmi_1_top])
                run_id_list = []
                for objA in final_1A:
                    run_id = objA.run
                    run_id_list.append(run_id)
            if gender_1 == "Not specify" and geo_1 != "Not specify":
                final_1A = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND GeoLocation = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_1, geo_1, age_1_bottom, age_1_top, bmi_1_bottom, bmi_1_top])
                run_id_list = []
                for objA in final_1A:
                    run_id = objA.run
                    run_id_list.append(run_id)
            if gender_1 != "Not specify" and geo_1 == "Not specify":
                final_1A = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Sex = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_1, gender_1, age_1_bottom, age_1_top, bmi_1_bottom, bmi_1_top])
                run_id_list = []
                for objA in final_1A:
                    run_id = objA.run
                    run_id_list.append(run_id)
            if gender_1 == "Not specify" and geo_1 == "Not specify":
                final_1A = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_1, age_1_bottom, age_1_top, bmi_1_bottom, bmi_1_top])
                run_id_list = []
                for objA in final_1A:
                    run_id = objA.run
                    run_id_list.append(run_id)
            with open(list_A_path, 'w') as fA:
                for each in run_id_list:
                    fA.write(each + '\n')
            fA.close()

            # ======================================================================== Group B ==============================================================================================================

            if gender_2 != "Not specify" and geo_2 != "Not specify":
                final_2A = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Sex = %s AND GeoLocation = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_2, gender_2, geo_2, age_2_bottom, age_2_top, bmi_2_bottom, bmi_2_top])
                run_id_list = []
                for objA in final_2A:
                    run_id = objA.run
                    run_id_list.append(run_id)
            if gender_2 == "Not specify" and geo_2 != "Not specify":
                final_2A = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND GeoLocation = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_2, geo_2, age_2_bottom, age_2_top, bmi_2_bottom, bmi_2_top])
                run_id_list = []
                for objA in final_2A:
                    run_id = objA.run
                    run_id_list.append(run_id)
            if gender_2 != "Not specify" and geo_2 == "Not specify":
                final_2A = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Sex = %s AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_2, gender_2, age_2_bottom, age_2_top, bmi_2_bottom, bmi_2_top])
                run_id_list = []
                for objA in final_2A:
                    run_id = objA.run
                    run_id_list.append(run_id)
            if gender_2 == "Not specify" and geo_2 == "Not specify":
                final_2A = Metadatatable.objects.raw(
                    "SELECT * FROM metadataTable WHERE run IN (SELECT run FROM phenotypeTable where phenotype = %s) AND Age BETWEEN %s AND %s AND BMI BETWEEN %s AND %s ", [phenotype_2, age_2_bottom, age_2_top, bmi_2_bottom, bmi_2_top])
                run_id_list = []
                for objA in final_2A:
                    run_id = objA.run
                    run_id_list.append(run_id)
            with open(list_B_path, 'w') as fB:
                for each in run_id_list:
                    fB.write(each + '\n')
            fB.close()

    # ===================================== Start analysis =============================================

            start(list_A_path, list_B_path, tempfolder)
            Reset_form(tempfolder)
            os.chdir(tempfolder)
            os.system(
                'Rscript /home/kaimin/microbiota-website/Src/filter/S_alpha_beta.R')
            os.system(
                'Rscript /home/kaimin/microbiota-website/Src/filter/G_alpha_beta.R')
            os.system('lefse_format_input.py G_A+B.csv G_A+B.in -c 1 -u 2')
            os.system('lefse_run.py G_A+B.in G_A+B.res')
            os.system('lefse_plot_res.py G_A+B.res G_A+B.png --dpi 300')
            os.system(
                'lefse_plot_cladogram.py G_A+B.res G_A+B.cladogram.png --format png --dpi 300')
            os.system('lefse_format_input.py S_A+B.csv S_A+B.in -c 1 -u 2')
            os.system('lefse_run.py G_A+B.in S_A+B.res')
            os.system('lefse_plot_res.py S_A+B.res S_A+B.png --dpi 300')
            os.system(
                'lefse_plot_cladogram.py S_A+B.res S_A+B.cladogram.png --format png --dpi 300')

    # =============================== Check LEfSe image if empty =======================================

            if not os.path.getsize('S_A+B.png'):
                os.remove('S_A+B.png')
                shutil.copyfile(
                    '/home/kaimin/microbiota-website/Src/media/icon.png', './S_A+B.png')
            if not os.path.getsize('G_A+B.png'):
                os.remove('G_A+B.png')
                shutil.copyfile(
                    '/home/kaimin/microbiota-website/Src/media/icon.png', './G_A+B.png')

    # =============================== Move & transform others image ==================================

            # Species
            os.chdir("/home/kaimin/microbiota-website/Src/")
            os.replace(tempfolder + 'S_A+B.png', folderpath + 'S_A+B.png')
            os.replace(tempfolder + 'G_A+B.png', folderpath + 'G_A+B.png')
            os.replace(tempfolder + 'S_A+B.cladogram.png',
                       folderpath + 'S_A+B.cladogram.png')
            os.replace(tempfolder + 'G_A+B.cladogram.png',
                       folderpath + 'G_A+B.cladogram.png')
            os.replace(tempfolder + 'S_alpha_chao1.pdf',
                       folderpath + 'S_alpha_chao1.pdf')
            pages_S_chao1 = convert_from_path(
                folderpath + 'S_alpha_chao1.pdf', 500)
            for page in pages_S_chao1:
                page.save(folderpath + 'S_alpha_chao1.jpg', 'JPEG')
            os.replace(tempfolder + 'S_alpha_shannon.pdf',
                       folderpath + 'S_alpha_shannon.pdf')
            pages_S_shannon = convert_from_path(
                folderpath + 'S_alpha_shannon.pdf', 500)
            for page in pages_S_shannon:
                page.save(folderpath + 'S_alpha_shannon.jpg', 'JPEG')
            '''
            os.replace(tempfolder + 'S_beta.pdf',
                       folderpath + 'S_beta.pdf')
            pages_S_beta = convert_from_path(
                folderpath + 'S_beta.pdf', 500)
            for page in pages_S_beta:
                page.save(folderpath + 'S_beta.jpg', 'JPEG')
            '''
            # Genus
            os.replace(tempfolder + 'G_alpha_chao1.pdf',
                       folderpath + 'G_alpha_chao1.pdf')
            pages_G_chao1 = convert_from_path(
                folderpath + 'G_alpha_chao1.pdf', 500)
            for page in pages_G_chao1:
                page.save(folderpath + 'G_alpha_chao1.jpg', 'JPEG')
            os.replace(tempfolder + 'G_alpha_shannon.pdf',
                       folderpath + 'G_alpha_shannon.pdf')
            pages_G_shannon = convert_from_path(
                folderpath + 'G_alpha_shannon.pdf', 500)
            for page in pages_G_shannon:
                page.save(folderpath + 'G_alpha_shannon.jpg', 'JPEG')
            '''
            os.replace(tempfolder + 'G_beta.pdf',
                       folderpath + 'G_beta.pdf')
            pages_G_beta = convert_from_path(
                folderpath + 'G_beta.pdf', 500)
            for page in pages_G_beta:
                page.save(folderpath + 'G_beta.jpg', 'JPEG')
            '''
    # =============================== Remove meta file ==================================

            os.remove(list_A_path)
            os.remove(list_B_path)
            return JsonResponse({'folderpath': folderpath_2})
