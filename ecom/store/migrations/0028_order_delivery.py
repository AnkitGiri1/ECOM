# Generated by Django 2.1.5 on 2020-08-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.FloatField(null=True),
        ),
    ]