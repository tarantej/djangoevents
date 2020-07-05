# Generated by Django 3.0.7 on 2020-07-02 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=200)),
                ('eventDate', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('eventDescription', models.TextField(blank=True)),
            ],
        ),
    ]