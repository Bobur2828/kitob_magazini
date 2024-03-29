# Generated by Django 5.0.2 on 2024-02-06 22:03

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_book', '0006_alter_obuna_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=500)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'kategoriyalar',
            },
        ),
        migrations.AlterModelOptions(
            name='izoh',
            options={'verbose_name': 'Izoh', 'verbose_name_plural': 'Izohlar'},
        ),
        migrations.AlterModelOptions(
            name='obuna',
            options={'verbose_name': 'Obuna', 'verbose_name_plural': 'Obunalar'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuslar'},
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=500)),
                ('avtor', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Profile_photo')),
                ('print_date', models.DateField(blank=True, null=True)),
                ('data_created', models.DateTimeField(default=datetime.datetime.now)),
                ('data_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='my_book.category')),
            ],
            options={
                'verbose_name': 'Kitob',
                'verbose_name_plural': 'Kitoblar',
            },
        ),
    ]
