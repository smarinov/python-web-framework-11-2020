# Generated by Django 3.1.3 on 2020-11-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_pet_passport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(upload_to='public/pets'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='passport',
            field=models.FileField(upload_to='private/documents'),
        ),
    ]