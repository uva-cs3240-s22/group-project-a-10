# Generated by Django 4.0.2 on 2022-05-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordofmouth', '0009_recipe_cook_time_metric_recipe_prep_time_metric'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cook_time_minutes_conversion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time_minutes_conversion',
            field=models.IntegerField(default=0),
        ),
    ]
