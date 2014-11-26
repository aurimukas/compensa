# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(default=b'', max_length=256, null=True, verbose_name='Brand', blank=True)),
                ('model', models.CharField(default=b'', max_length=256, null=True, verbose_name='Model', blank=True)),
                ('car_reg', models.CharField(default=None, max_length=16, null=True, verbose_name='Car reg. number', blank=True)),
                ('vin', models.CharField(default=None, max_length=32, null=True, verbose_name='VIN number', blank=True)),
                ('production_year', models.SmallIntegerField(default=None, max_length=8, null=True, verbose_name='Construction year', blank=True)),
                ('first_registration_date', models.DateTimeField(default=None, null=True, verbose_name='First Registration', blank=True)),
                ('capicity', models.IntegerField(default=None, max_length=8, null=True, verbose_name='cm3', blank=True)),
                ('power', models.IntegerField(default=None, max_length=8, null=True, verbose_name='KW', blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, blank=True, null=True, verbose_name='Price')),
                ('type', models.CharField(default=b'', max_length=16, null=True, verbose_name='Vehicle Category Name', blank=True)),
                ('type_id', models.CharField(default=b'', max_length=32, null=True, verbose_name='Vehicle Category id', blank=True)),
                ('weight', models.DecimalField(decimal_places=3, default=None, max_digits=8, blank=True, null=True, verbose_name='Weight')),
                ('seats', models.SmallIntegerField(default=None, max_length=4, null=True, verbose_name='Seats', blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2014, 11, 23, 7, 12, 56, 919704, tzinfo=utc), verbose_name='Created', auto_now_add=True)),
                ('updated', models.DateTimeField(default=datetime.datetime(2014, 11, 23, 7, 12, 56, 919729, tzinfo=utc), verbose_name='Updated', auto_now=True)),
                ('status', models.SmallIntegerField(default=1, max_length=4, verbose_name='Status', blank=True, choices=[(1, 'Started to synchronize'), (2, 'Successfully synchronized'), (3, 'Error in synchronization')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(default=None, max_length=32, verbose_name='Code')),
                ('created', models.DateTimeField(default=datetime.datetime(2014, 11, 23, 7, 12, 56, 918651, tzinfo=utc), verbose_name='Created', auto_now_add=True)),
                ('updated', models.DateTimeField(default=datetime.datetime(2014, 11, 23, 7, 12, 56, 918684, tzinfo=utc), verbose_name='Updated', auto_now=True)),
                ('requested_reg_numbers', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of reg. numbers.', verbose_name='Car Reg. Number')),
                ('user', models.ForeignKey(verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='car',
            name='request',
            field=models.ForeignKey(to='com_local.Request'),
            preserve_default=True,
        ),
    ]
