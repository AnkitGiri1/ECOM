# Generated by Django 2.1.5 on 2020-08-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200803_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/images/', width_field=42),
        ),
    ]
