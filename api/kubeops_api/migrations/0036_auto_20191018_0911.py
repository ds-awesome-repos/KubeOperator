# Generated by Django 2.1.2 on 2019-10-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0035_auto_20191017_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clusterhealthhistory',
            name='date_type',
            field=models.CharField(choices=[('HOUR', 'HOUR'), ('DAY', 'DAY')], default='HOUR', max_length=255),
        ),
    ]