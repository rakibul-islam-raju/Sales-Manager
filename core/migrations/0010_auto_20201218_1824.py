# Generated by Django 3.1.2 on 2020-12-18 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20201218_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchaseproduct',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='sellproduct',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['-id']},
        ),
    ]