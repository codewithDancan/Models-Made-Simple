# Generated by Django 5.0 on 2024-02-29 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='posts',
            field=models.ImageField(default='C:/Users/Dancan Ngaga/Desktop/modelsmadesimple/static/img/.blank_image.png', upload_to='posts'),
        ),
    ]
