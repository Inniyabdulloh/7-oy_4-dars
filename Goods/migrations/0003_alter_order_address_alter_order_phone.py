# Generated by Django 5.0.7 on 2024-07-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0002_alter_productenter_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
