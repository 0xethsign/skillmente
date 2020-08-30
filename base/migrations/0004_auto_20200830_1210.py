# Generated by Django 3.0.4 on 2020-08-30 12:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20200828_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form2',
            name='t_contact',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='In the format 9999999999', regex='^\\+?1?\\d{10,12}$')]),
        ),
    ]
