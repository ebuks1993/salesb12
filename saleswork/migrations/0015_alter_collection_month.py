# Generated by Django 4.1.7 on 2023-03-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleswork', '0014_alter_collection_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='month',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
