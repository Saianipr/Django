# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('tech', 'Techinical'), ('art', 'Art'), ('sports', 'Sports'), ('cultural', 'Custoral')], help_text='haii this is help', max_length=3)),
                ('pic', models.BinaryField()),
                ('is_college', models.BooleanField()),
                ('date_reg', models.DateField(auto_now=True)),
                ('budget', models.DecimalField(decimal_places=4, max_digits=5)),
                ('duration', models.DurationField()),
                ('email', models.EmailField(max_length=254)),
                ('document', models.FileField(upload_to='uploads/')),
                ('image', models.ImageField(upload_to=b'')),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
    ]