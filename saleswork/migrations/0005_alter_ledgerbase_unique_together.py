# Generated by Django 4.1.7 on 2023-03-17 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saleswork', '0004_rename_coded_ledgerbase_group_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ledgerbase',
            unique_together={('semi', 'LEDGER', 'TEAM', 'STATUS', 'GROUP')},
        ),
    ]