# Generated by Django 2.2 on 2022-05-11 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0005_stock_datefield'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='reoder_level',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
