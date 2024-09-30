# Generated by Django 5.1.1 on 2024-09-30 19:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('payment', models.CharField(max_length=200, null=True)),
                ('taxprice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('shippingPrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('isPaid', models.BooleanField(default=False)),
                ('paidAt', models.DateTimeField(blank=True, null=True)),
                ('isDeliverd', models.BooleanField(default=False)),
                ('deliveredAt', models.DateTimeField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('qty', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.CharField(max_length=255, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=7)),
                ('comment', models.TextField(null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShippiingAddress',
            fields=[
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('postalCode', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('shippingPrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.order')),
            ],
        ),
    ]
