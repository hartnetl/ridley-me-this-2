# Generated by Django 3.2 on 2022-01-19 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_alter_turtles_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turtles',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.turtlespecies'),
        ),
    ]