# Generated by Django 2.0 on 2019-01-03 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0013_auto_20190104_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='home_address',
        ),
        migrations.RemoveField(
            model_name='member',
            name='working_school_address',
        ),
        migrations.AddField(
            model_name='member',
            name='dwelling',
            field=models.CharField(choices=[('N', '台灣北部'), ('M', '台灣中部'), ('S', '台灣南部'), ('E', '台灣東部'), ('O', '其他')], default='N', max_length=10),
        ),
    ]