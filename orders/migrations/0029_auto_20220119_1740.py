# Generated by Django 3.2 on 2022-01-19 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_alter_turtles_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurtleSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('friendly_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Species',
            },
        ),
    ]
