# Generated by Django 2.0 on 2018-12-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_component_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='number',
        ),
        migrations.AddField(
            model_name='material',
            name='number_needed',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
