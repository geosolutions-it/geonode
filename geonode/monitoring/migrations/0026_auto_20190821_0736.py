# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-21 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0025_auto_20190813_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestevent',
            name='user_anonymous',
        ),
        migrations.AddField(
            model_name='requestevent',
            name='user_username',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='metricvalue',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metric_values', to='monitoring.MonitoredResource'),
        ),
        migrations.AlterField(
            model_name='monitoredresource',
            name='type',
            field=models.CharField(choices=[('','No resource'), ('layer','Layer'), ('map','Map'), ('resource_base','Resource base'), ('document','Document'), ('style','Style'), ('admin','Admin'), ('url','URL'), ('other','Other')], default='', max_length=255),
        ),
    ]
