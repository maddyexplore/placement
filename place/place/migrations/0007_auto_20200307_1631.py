# Generated by Django 3.0.3 on 2020-03-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_auto_20200307_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slogin',
            name='cgpa',
            field=models.CharField(max_length=20),
        ),
    ]
