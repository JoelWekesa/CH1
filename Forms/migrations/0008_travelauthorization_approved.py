# Generated by Django 3.2 on 2021-04-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0007_travelauthorizationsupervisor_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelauthorization',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
