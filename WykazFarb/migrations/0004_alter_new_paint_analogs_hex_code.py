# Generated by Django 3.2.22 on 2023-12-08 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WykazFarb', '0003_alter_new_paint_analogs_hex_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_paint_analogs',
            name='Hex_Code',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
