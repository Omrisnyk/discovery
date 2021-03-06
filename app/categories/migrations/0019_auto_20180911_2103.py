# Generated by Django 2.0.2 on 2018-09-11 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0018_auto_20180829_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='ordering_guide',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='poc',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Tier'),
        ),
    ]
