# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-07-10 12:42
from __future__ import unicode_literals

import datetime
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import eav.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='User-friendly attribute name', max_length=100, verbose_name='name')),
                ('slug', eav.fields.EavSlugField(help_text='Short unique attribute label', verbose_name='slug')),
                ('description', models.CharField(blank=True, help_text='Short description', max_length=256, null=True, verbose_name='description')),
                ('type', models.CharField(blank=True, max_length=20, null=True, verbose_name='type')),
                ('datatype', eav.fields.EavDatatypeField(choices=[(b'text', 'Text'), (b'float', 'Float'), (b'int', 'Integer'), (b'date', 'Date'), (b'bool', 'True / False'), (b'object', 'Django Object'), (b'enum', 'Multiple Choice')], max_length=6, verbose_name='data type')),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('required', models.BooleanField(default=False, verbose_name='required')),
            ],
            options={
                'ordering': ['name'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='EnumGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='EnumValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='value')),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_id', models.IntegerField()),
                ('value_text', models.TextField(blank=True, null=True)),
                ('value_float', models.FloatField(blank=True, null=True)),
                ('value_int', models.IntegerField(blank=True, null=True)),
                ('value_date', models.DateTimeField(blank=True, null=True)),
                ('value_bool', models.NullBooleanField()),
                ('generic_value_id', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eav.Attribute', verbose_name='attribute')),
                ('entity_ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value_entities', to='contenttypes.ContentType')),
                ('generic_value_ct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='value_values', to='contenttypes.ContentType')),
                ('value_enum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eav_values', to='eav.EnumValue')),
            ],
        ),
        migrations.AddField(
            model_name='enumgroup',
            name='enums',
            field=models.ManyToManyField(to='eav.EnumValue', verbose_name='enum group'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='enum_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eav.EnumGroup', verbose_name='choice group'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='site'),
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together=set([('site', 'slug')]),
        ),
    ]
