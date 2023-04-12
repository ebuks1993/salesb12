# Generated by Django 4.1.7 on 2023-03-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleswork', '0011_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('pointer', models.IntegerField()),
                ('fullstatus', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=150)),
            ],
        ),
    ]