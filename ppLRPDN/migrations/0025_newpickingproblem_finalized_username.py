# Generated by Django 3.2.21 on 2023-10-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppLRPDN', '0024_alter_newpickingproblem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpickingproblem',
            name='finalized_username',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
