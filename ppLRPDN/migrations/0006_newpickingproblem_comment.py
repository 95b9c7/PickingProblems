# Generated by Django 3.2.21 on 2023-10-02 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppLRPDN', '0005_auto_20231002_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpickingproblem',
            name='comment',
            field=models.CharField(default='N/A', max_length=200),
            preserve_default=False,
        ),
    ]