# Generated by Django 3.2.22 on 2023-12-19 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WykazFarb', '0005_new_paint_analogs_style'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_paint_analogs',
            name='Style',
        ),
    ]
