# Generated by Django 2.1.5 on 2020-08-03 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]
