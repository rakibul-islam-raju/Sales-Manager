# Generated by Django 3.1.2 on 2021-01-21 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20201221_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproduct',
            name='sack',
            field=models.IntegerField(choices=[(5, '5 kg'), (35, '35 kg'), (37, '37 kg'), (50, '50 kg'), (55, '55 kg'), (60, '60 kg')]),
        ),
    ]