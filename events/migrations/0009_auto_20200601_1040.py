# Generated by Django 3.0.6 on 2020-05-31 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20200601_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
        migrations.AddField(
            model_name='company',
            name='company_id',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='company',
            name='company_name_id',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='company',
            name='id',
            field=models.AutoField(auto_created=True, default=8890, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]