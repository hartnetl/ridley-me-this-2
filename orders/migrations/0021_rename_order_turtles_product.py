# Generated by Django 3.2 on 2022-01-18 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20220118_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turtles',
            old_name='order',
            new_name='product',
        ),
    ]
