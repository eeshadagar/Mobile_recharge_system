# Generated by Django 4.1.3 on 2022-12-21 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_detail_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='productID',
        ),
    ]
