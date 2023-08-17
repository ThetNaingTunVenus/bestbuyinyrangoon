# Generated by Django 4.1.7 on 2023-04-02 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_cartproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_by', models.CharField(max_length=255)),
                ('shipping_address', models.CharField(default='local', max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subtotal', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('tax', models.PositiveIntegerField()),
                ('all_total', models.PositiveIntegerField()),
                ('ordered_staus', models.CharField(choices=[('Ordering', 'Ordering'), ('Accept', 'Accept'), ('Cash', 'Cash'), ('Credit', 'Credit'), ('Consignment', 'Consignment'), ('Complete', 'Complete')], default='Ordering', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.cart')),
            ],
        ),
    ]