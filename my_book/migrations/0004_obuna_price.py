# Generated by Django 5.0.2 on 2024-02-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_book', '0003_obuna_alter_status_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='obuna',
            name='price',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
