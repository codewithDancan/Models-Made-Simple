# Generated by Django 5.0 on 2024-03-01 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_todolist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='todolists', to='client.client'),
        ),
    ]
