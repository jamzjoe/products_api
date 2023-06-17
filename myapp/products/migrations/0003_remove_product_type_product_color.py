# Generated by Django 4.2.2 on 2023-06-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='blue', max_length=100),
        ),
    ]
