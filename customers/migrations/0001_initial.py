# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-29 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
    ]