# Generated by Django 2.2.4 on 2020-09-13 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='Customer_name',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
