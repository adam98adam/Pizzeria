# Generated by Django 3.2 on 2021-04-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210420_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemtemplate',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
