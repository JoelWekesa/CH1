# Generated by Django 3.2 on 2021-04-14 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0004_auto_20210414_0859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='other',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Other'},
        ),
        migrations.AlterModelOptions(
            name='travelauthorization',
            options={'ordering': ['-id'], 'verbose_name_plural': 'TravelAuthorization'},
        ),
        migrations.CreateModel(
            name='TravelAuthorizationSupervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forms.travelauthorization')),
            ],
            options={
                'verbose_name_plural': 'TravelAuthorizationSupervisor',
                'ordering': ['-id'],
            },
        ),
    ]
