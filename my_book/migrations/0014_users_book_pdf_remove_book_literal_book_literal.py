# Generated by Django 5.0.3 on 2024-03-30 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_book', '0013_alter_country_options_country_content_country_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('is_client', models.BooleanField(default=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='product'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='literal',
        ),
        migrations.AddField(
            model_name='book',
            name='literal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='literal', to='my_book.country'),
        ),
    ]
