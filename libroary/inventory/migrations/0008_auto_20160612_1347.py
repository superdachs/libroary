# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20160612_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('foundet', models.DateField()),
                ('disbanded', models.DateField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Interpret',
            fields=[
                ('author_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.Author')),
                ('band', models.ManyToManyField(to='inventory.Band')),
            ],
            bases=('inventory.author',),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.Media')),
                ('media', models.CharField(max_length=30)),
                ('media_tyoe', models.CharField(max_length=30)),
                ('band', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Band')),
                ('languages', models.ManyToManyField(to='inventory.Language')),
            ],
            bases=('inventory.media',),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('length_hour', models.IntegerField()),
                ('length_minutes', models.IntegerField()),
                ('length_seconds', models.IntegerField()),
                ('interpret', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Interpret')),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='titles',
            field=models.ManyToManyField(to='inventory.Title'),
        ),
    ]
