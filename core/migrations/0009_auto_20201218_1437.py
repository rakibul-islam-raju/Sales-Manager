# Generated by Django 3.1.2 on 2020-12-18 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201218_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchaseproduct',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterModelOptions(
            name='sellproduct',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['date_added']},
        ),
    ]