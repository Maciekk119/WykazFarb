# Generated by Django 3.2.22 on 2023-11-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WykazFarb', '0004_alter_paint_sets_paints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paint_sets',
            name='paints',
            field=models.ManyToManyField(to='WykazFarb.Paint'),
        ),
    ]