# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OtuTable(models.Model):
    # Field name made lowercase.
    run_id = models.CharField(
        db_column='Run_id', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    feature_id = models.TextField(
        db_column='Feature_id', blank=True, null=True)
    # Field name made lowercase.
    taxa = models.TextField(db_column='Taxa', blank=True, null=True)
    # Field name made lowercase.
    otu = models.IntegerField(db_column='OTU', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OTU_table'


class OtuTableBackup(models.Model):
    # Field name made lowercase.
    run_id = models.CharField(
        db_column='Run_id', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    feature_id = models.TextField(
        db_column='Feature_id', blank=True, null=True)
    # Field name made lowercase.
    taxa = models.TextField(db_column='Taxa', blank=True, null=True)
    # Field name made lowercase.
    otu = models.IntegerField(db_column='OTU', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OTU_table_backup'


class RunOfOtuTable(models.Model):
    # Field name made lowercase.
    run_id = models.CharField(
        db_column='Run_id', max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Run_of_OTU_table'


class Metadatatable(models.Model):
    # Field name made lowercase.
    run = models.CharField(db_column='Run', primary_key=True, max_length=12)
    # Field name made lowercase.
    sex = models.CharField(
        db_column='Sex', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    # Field name made lowercase.
    bmi = models.FloatField(db_column='BMI', blank=True, null=True)
    # Field name made lowercase.
    geolocation = models.CharField(
        db_column='GeoLocation', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    race = models.CharField(
        db_column='Race', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    srastudy = models.CharField(
        db_column='SRAStudy', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    bioproject = models.CharField(
        db_column='BioProject', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    biosample = models.CharField(
        db_column='BioSample', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    librarylayout = models.CharField(
        db_column='LibraryLayout', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    platform = models.CharField(
        db_column='Platform', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    model = models.CharField(
        db_column='Model', max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadataTable'


class Phenotypetable(models.Model):
    # Field name made lowercase.
    run = models.TextField(db_column='Run', blank=True, null=True)
    # Field name made lowercase.
    phenotype = models.TextField(db_column='Phenotype', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phenotypeTable'
