# Generated by Django 3.2.21 on 2023-10-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppLRPDN', '0025_newpickingproblem_finalized_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=100)),
                ('first_name', models.CharField(default='-', max_length=100)),
                ('last_name', models.CharField(default='-', max_length=100)),
                ('employee_id', models.CharField(default='-', max_length=100)),
                ('as400_username', models.CharField(default='-', max_length=100)),
            ],
        ),
    ]
