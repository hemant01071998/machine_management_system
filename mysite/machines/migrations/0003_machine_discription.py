# Generated by Django 4.2.2 on 2023-08-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_machine_end_time_machine_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='discription',
            field=models.TextField(max_length=500, null=True),
        ),
    ]