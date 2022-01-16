# Generated by Django 3.2 on 2022-01-16 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20220115_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_ordered',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='item',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='orders.order'),
        ),
    ]
