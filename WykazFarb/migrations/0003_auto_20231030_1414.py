# Generated by Django 3.2.22 on 2023-10-30 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WykazFarb', '0002_auto_20231009_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paint',
            name='analog',
        ),
        migrations.AddField(
            model_name='paint',
            name='analog',
            field=models.ManyToManyField(related_name='_WykazFarb_paint_analog_+', to='WykazFarb.Paint'),
        ),
    ]