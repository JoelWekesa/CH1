# Generated by Django 3.2 on 2021-04-09 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_taxilogisticssupervisor_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisorapprovedpurchaserequisitions',
            name='requisition',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.purchaserequisition'),
        ),
    ]
