# Generated by Django 5.1 on 2024-08-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0004_profile_old_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=800, null=True),
        ),
    ]
