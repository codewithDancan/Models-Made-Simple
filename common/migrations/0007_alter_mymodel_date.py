# Generated by Django 5.0 on 2024-03-01 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_mymodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 1, 18, 13, 51, 577192, tzinfo=datetime.timezone.utc)),
        ),
    ]
