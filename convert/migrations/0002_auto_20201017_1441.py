# Generated by Django 3.0.8 on 2020-10-17 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
