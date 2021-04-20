# Generated by Django 3.2 on 2021-04-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_pizzaside_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzasize',
            name='diameter',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='pizzasize',
            name='ingredientcostfactor',
            field=models.FloatField(unique=True),
        ),
        migrations.AlterField(
            model_name='pizzasize',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='pizzasize',
            name='price',
            field=models.FloatField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='customer',
            field=models.BooleanField(default=True),
        ),
    ]