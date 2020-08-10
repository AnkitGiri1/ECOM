# Generated by Django 2.1.5 on 2020-08-08 12:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0022_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user_id',
        ),
        migrations.AddField(
            model_name='order_items',
            name='order_id',
            field=models.ForeignKey(on_delete='CASCADE', to='store.order'),
        ),
        migrations.AddField(
            model_name='order_items',
            name='product_id',
            field=models.ForeignKey(on_delete='CASCADE', to='store.product'),
        ),
        migrations.AddField(
            model_name='order_items',
            name='user_id',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]