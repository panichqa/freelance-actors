# Generated by Django 5.1.1 on 2024-09-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors_agency', '0004_alter_character_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='actoragency',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
