# Generated by Django 2.2.20 on 2021-08-01 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20210801_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
    ]
