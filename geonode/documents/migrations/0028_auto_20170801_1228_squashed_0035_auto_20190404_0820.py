# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    replaces = [('documents', '0028_auto_20170801_1228'), ('documents', '0029_auto_20180301_1947'), ('documents', '0030_auto_20180302_0430'), ('documents', '0031_auto_20180409_1238'), ('documents', '0032_auto_20180412_0822'), ('documents', '0033_auto_20180414_2120'), ('documents', '0034_auto_20190329_1652'), ('documents', '0035_auto_20190404_0820')]

    dependencies = [
        ('documents', '27_drop_resource_columns_from_document_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='abstract_en',
            field=models.TextField(blank=True, help_text='brief narrative summary of the content of the resource(s)', max_length=2000, null=True, verbose_name='abstract'),
        ),
        migrations.AlterField(
            model_name='document',
            name='data_quality_statement_en',
            field=models.TextField(blank=True, help_text="general explanation of the data producer's knowledge about the lineage of a dataset", max_length=2000, null=True, verbose_name='data quality statement'),
        ),
        migrations.AlterField(
            model_name='document',
            name='purpose_en',
            field=models.TextField(blank=True, help_text='summary of the intentions with which the resource(s) was developed', max_length=500, null=True, verbose_name='purpose'),
        ),
        migrations.AlterField(
            model_name='document',
            name='supplemental_information_en',
            field=models.TextField(default='No information provided', help_text='any other descriptive information about the dataset', max_length=2000, null=True, verbose_name='supplemental information'),
        ),
        migrations.AlterModelManagers(
            name='document',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelManagers(
            name='document',
            managers=[
            ],
        ),
        migrations.AlterModelOptions(
            name='document',
            options={},
        ),
        migrations.AlterModelManagers(
            name='document',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
