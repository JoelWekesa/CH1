# Generated by Django 3.2 on 2021-04-19 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0024_businessexpensereport_finance_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessexpensereport',
            name='date_approved',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
