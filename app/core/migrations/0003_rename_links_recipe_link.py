# Generated by Django 3.2.25 on 2025-04-21 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='links',
            new_name='link',
        ),
    ]
