# Generated by Django 4.1.3 on 2022-11-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='bio',
            field=models.TimeField(max_length=250, null=True),
        ),
    ]