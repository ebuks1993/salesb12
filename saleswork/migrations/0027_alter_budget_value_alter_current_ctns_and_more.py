# Generated by Django 4.1.7 on 2023-04-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleswork', '0026_alter_budget_value_alter_current_fyear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='value',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='current',
            name='ctns',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='current',
            name='fyear',
            field=models.IntegerField(null=True),
        ),
    ]
