# Generated by Django 5.0.3 on 2024-03-11 09:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_alter_products_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('A01', 'A01'), ('A02', 'A02'), ('A03', 'A03'), ('A04', 'A04'), ('B05', 'B05'), ('B06', 'B06'), ('B07', 'B07'), ('B08', 'B08'), ('C09', 'C09'), ('C10', 'C10'), ('C11', 'C11'), ('C12', 'C12'), ('D13', 'D13'), ('D14', 'D14'), ('D15', 'D15'), ('D16', 'D16')], default=0, max_length=3)),
                ('max_quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('product_quantity', models.IntegerField(default=0)),
                ('product_price', models.FloatField()),
                ('product_image', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.product')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
