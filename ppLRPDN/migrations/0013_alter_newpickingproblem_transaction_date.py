# Generated by Django 3.2.21 on 2023-10-06 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppLRPDN', '0012_delete_finalpickingproblem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpickingproblem',
            name='transaction_date',
            field=models.DateField(default='2001-01-01'),
        ),
    ]