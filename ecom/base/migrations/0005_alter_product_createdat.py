# Generated by Django 5.1.1 on 2024-09-30 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_product_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='createdAt',
            field=models.DateTimeField(null=True),
        ),
    ]
