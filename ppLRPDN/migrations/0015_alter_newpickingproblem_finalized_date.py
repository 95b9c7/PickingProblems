# Generated by Django 3.2.21 on 2023-10-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppLRPDN', '0014_newpickingproblem_finalized_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpickingproblem',
            name='finalized_date',
            field=models.DateField(),
        ),
    ]
