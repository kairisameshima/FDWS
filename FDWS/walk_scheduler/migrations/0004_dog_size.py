# Generated by Django 3.2 on 2021-04-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walk_scheduler', '0003_rename_walker_appointment_walker'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='size',
            field=models.CharField(blank=True, choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large')], max_length=20),
        ),
    ]
