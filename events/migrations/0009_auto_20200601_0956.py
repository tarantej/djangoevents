# Generated by Django 3.0.6 on 2020-05-31 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20200601_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='companyname',
        ),
    ]