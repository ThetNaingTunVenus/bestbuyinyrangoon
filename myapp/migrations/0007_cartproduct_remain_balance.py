# Generated by Django 4.1.7 on 2023-04-05 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_order_mobile_alter_order_ordered_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='remain_balance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
