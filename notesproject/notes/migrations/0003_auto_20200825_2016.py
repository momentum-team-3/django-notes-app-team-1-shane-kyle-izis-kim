# Generated by Django 3.1 on 2020-08-25 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200825_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(max_length=10000),
        ),
    ]