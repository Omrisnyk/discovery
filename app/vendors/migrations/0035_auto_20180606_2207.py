# Generated by Django 2.0.2 on 2018-06-06 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0034_auto_20180604_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poolmembership',
            name='contract_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='poolmembership',
            name='expiration_8a_date',
            field=models.DateField(null=True),
        ),
    ]