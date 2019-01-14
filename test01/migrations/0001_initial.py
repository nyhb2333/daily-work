# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileBrand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_text', models.CharField(max_length=255)),
                ('country_text', models.CharField(max_length=255)),
                ('sales', models.IntegerField(null=True)),
                ('thumbs', models.IntegerField(null=True)),
                ('haopins', models.IntegerField(null=True)),
                ('create_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobileProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_text', models.CharField(max_length=255)),
                ('scores', models.IntegerField()),
                ('brand', models.ForeignKey(related_query_name=b'product', related_name='products', to='test01.MobileBrand')),
            ],
            options={
                'ordering': ['-scores'],
                'default_related_name': 'ps',
            },
        ),
    ]
