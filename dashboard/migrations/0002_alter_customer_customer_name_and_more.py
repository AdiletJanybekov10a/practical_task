# Generated by Django 4.1.6 on 2023-02-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Customer name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_name',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Employee name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Order name'),
        ),
    ]
