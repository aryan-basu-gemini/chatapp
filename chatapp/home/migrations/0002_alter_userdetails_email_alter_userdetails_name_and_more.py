# Generated by Django 4.1.7 on 2023-08-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='password',
            field=models.CharField(max_length=40),
        ),
    ]
