# Generated by Django 3.2 on 2022-01-18 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_rename_order_turtles_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turtles',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turtles', to='orders.product'),
        ),
    ]
