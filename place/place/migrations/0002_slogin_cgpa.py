# Generated by Django 3.0.3 on 2020-03-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slogin',
            name='cgpa',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
