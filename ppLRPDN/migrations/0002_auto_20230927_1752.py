# Generated by Django 3.2.21 on 2023-09-27 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppLRPDN', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpickingproblem',
            name='id',
        ),
        migrations.AddField(
            model_name='newpickingproblem',
            name='part_number',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newpickingproblem',
            name='planner',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newpickingproblem',
            name='reference_number',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newpickingproblem',
            name='total_affected',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newpickingproblem',
            name='total_quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newpickingproblem',
            name='unit_type',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newpickingproblem',
            name='work_order',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newpickingproblem',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='newpickingproblem',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='newpickingproblem',
            name='time',
            field=models.TimeField(),
        ),
    ]
