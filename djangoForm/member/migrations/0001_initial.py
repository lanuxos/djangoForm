# Generated by Django 3.1.7 on 2021-08-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=100, null=True, verbose_name='First Name')),
                ('lastName', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lase Name')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date Of Birth')),
                ('workPlace', models.CharField(blank=True, max_length=100, null=True, verbose_name='Work Place')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('tel', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tel')),
            ],
        ),
    ]
