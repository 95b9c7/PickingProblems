# Generated by Django 3.2.21 on 2023-10-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppLRPDN', '0006_newpickingproblem_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpickingproblem',
            name='defect',
            field=models.CharField(choices=[('Dirty', 'Dirty'), ('Damaged', 'Damaged'), ('Wrong', 'Wrong'), ('Incomplete', 'Incomplete'), ('Excess', 'Excess'), ('Short', 'Short'), ('Expiration', 'Expiration'), ('Wrong UoM', 'Wrong UoM'), ('Other', 'Other'), ('WrngPrt', 'Wrong Part'), ('MxPrt', 'Mixed Part'), ('WrngQty', 'Wrong Quantity'), ('WrngLoc', 'Wrong Location'), ('Clearance', 'Clearance'), ('Photos', 'Photos'), ('Missing', 'Missing')], default='N/A', max_length=100),
        ),
    ]