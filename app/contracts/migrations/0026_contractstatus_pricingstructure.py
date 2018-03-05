# Generated by Django 2.0.2 on 2018-03-01 20:27

from django.db import migrations, models


def populate_contract_statuses(apps, schema_editor):
    ContractStatus = apps.get_model('contracts', 'ContractStatus')
    
    status_map = {
        'A': 'Additional Work',
        'B': 'Supplemental Agreement for work within scope',
        'C': 'Funding Only Action',
        'D': 'Change Order',
        'E': 'Terminated for Default',
        'F': 'Terminated for Convenience',
        'G': 'Exercise an Option',
        'H': 'Definitize Letter Contract',
        'J': 'Novation Agreement',
        'K': 'Close out',
        'L': 'Definitize Letter Contract',
        'M': 'Other Adminitrative Action',
        'N': 'Legal Contract Cancellation',
        'P': 'Representation of non-Novated Merger/Acquisitoin',
        'R': 'Rerepresentation',
        'S': 'Change PIID',
        'T': 'Transfer Action',
        'V': 'Vendor DUNS Change',
        'W': 'Vendor Address Change',
        'X': 'Terminated for Cause',
        'C1': 'Completed',
        'C2': 'Current',
    }
    for key, value in status_map.items():
        ContractStatus.objects.create(code=key, name=value)


def populate_pricing_structures(apps, schema_editor):
    PricingStructure = apps.get_model('contracts', 'PricingStructure')
    
    structure_map = {
        'A': 'Fixed Price Redetermination',
        'B': 'Fixed Price Level of Effort',
        'J': 'Firm Fixed Price',
        'K': 'Fixed Price with Economic Price Adjustment',
        'L': 'Fixed Price Incentive',
        'M': 'Fixed Price Award Fee',
        'R': 'Cost Plus Award Fee',
        'S': 'Cost No Fee',
        'T': 'Cost Sharing',
        'U': 'Cost Plus Fixed Fee',
        'V': 'Cost Plus Incentive Fee',
        'Y': 'Time and Materials',
        'Z': 'Labor Hours',
        '1': 'Order Dependent',
        '2': 'Combination',
        '3': 'Other',
    }
    for key, value in structure_map.items():
        PricingStructure.objects.create(code=key, name=value)


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0025_auto_20180211_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractStatus',
            fields=[
                ('code', models.CharField(max_length=5, null=False, primary_key=True)),
                ('name', models.CharField(max_length=128, null=False)),
            ],
        ),
        migrations.RunPython(populate_contract_statuses),
        migrations.CreateModel(
            name='PricingStructure',
            fields=[
                ('code', models.CharField(max_length=5, null=False, primary_key=True)),
                ('name', models.CharField(max_length=128, null=False)),
            ],
        ),
        migrations.RunPython(populate_pricing_structures),
    ]
