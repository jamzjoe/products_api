# Generated by Django 4.2.2 on 2023-06-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
