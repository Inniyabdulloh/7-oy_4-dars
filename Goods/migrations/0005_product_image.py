# Generated by Django 5.0.7 on 2024-08-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0004_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
    ]
