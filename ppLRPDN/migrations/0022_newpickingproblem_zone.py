# Generated by Django 3.2.21 on 2023-10-18 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppLRPDN', '0021_alter_newpickingproblem_transaction_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpickingproblem',
            name='zone',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
