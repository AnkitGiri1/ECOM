# Generated by Django 2.1.5 on 2020-08-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='no', max_length=16),
        ),
    ]
