# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-01 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('B_Title', models.CharField(max_length=125)),
                ('B_Author', models.CharField(max_length=125)),
                ('B_pages', models.CharField(max_length=125)),
                ('B_Price', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_Name', models.CharField(max_length=125)),
                ('C_Model', models.CharField(max_length=125)),
                ('C_Loanch', models.DateField()),
                ('C_Price', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_Name', models.CharField(max_length=125)),
                ('F_Price', models.CharField(max_length=125)),
            ],
        ),
    ]
