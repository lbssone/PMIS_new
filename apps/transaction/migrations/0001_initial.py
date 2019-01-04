# Generated by Django 2.0 on 2019-01-04 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0016_auto_20190104_1144'),
        ('inventory', '0021_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('total_price', models.PositiveIntegerField(blank=True, null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.Member')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Transaction_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.Transaction')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='products',
            field=models.ManyToManyField(through='transaction.Transaction_product', to='inventory.Product'),
        ),
    ]