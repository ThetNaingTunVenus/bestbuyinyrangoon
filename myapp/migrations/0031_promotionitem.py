# Generated by Django 4.2.4 on 2023-08-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_items_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=225)),
                ('price', models.CharField(max_length=225)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('promo_img', models.ImageField(blank=True, upload_to='promotion/')),
            ],
        ),
    ]
