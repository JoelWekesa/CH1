# Generated by Django 3.2 on 2021-05-26 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0027_auto_20210526_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Forms.leaveapplicationsupervisor'),
        ),
    ]