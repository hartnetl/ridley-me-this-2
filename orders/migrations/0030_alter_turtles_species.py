# Generated by Django 3.2 on 2022-01-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0029_auto_20220119_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turtles',
            name='species',
            field=models.CharField(choices=[('logger', 'Loggerhead'), ('green', 'Green'), ('leather', 'Leatherback'), ('flat', 'Flatback'), ('hawks', 'Hawksbill'), ('olive', 'Olive Ridley'), ('kemp', "Kemp's Ridley")], max_length=10),
        ),
    ]
