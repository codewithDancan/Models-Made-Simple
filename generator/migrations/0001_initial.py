# Generated by Django 5.0 on 2024-03-07 11:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last name')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=35, verbose_name='Word')),
                ('slug', models.CharField(max_length=50, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('cover', models.ImageField(blank=True, upload_to='book-covers', verbose_name='Cover')),
                ('publication_date', models.DateField(verbose_name='Publication date')),
                ('authors', models.ManyToManyField(related_name='books', to='generator.author', verbose_name='Authors')),
                ('tags', models.ManyToManyField(related_name='books', to='generator.tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(verbose_name='Borrow date')),
                ('returned_date', models.DateField(blank=True, null=True, verbose_name='Returned date')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.book', verbose_name='Book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Borrow',
                'verbose_name_plural': 'Borrows',
            },
        ),
    ]