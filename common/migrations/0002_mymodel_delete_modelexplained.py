# Generated by Django 5.0 on 2024-03-01 00:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('boolean', models.BooleanField(default=True, verbose_name='This a Boolean')),
                ('uuid1', models.UUIDField(default=uuid.uuid4)),
                ('uuid2', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='ModelExplained',
        ),
    ]
