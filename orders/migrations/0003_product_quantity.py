# Generated by Django 3.2 on 2022-01-10 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
