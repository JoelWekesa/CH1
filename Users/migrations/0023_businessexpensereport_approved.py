# Generated by Django 3.2 on 2021-04-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0022_businessexpensereportfinance'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessexpensereport',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
