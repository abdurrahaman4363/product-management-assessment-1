# Generated by Django 4.2.7 on 2024-10-04 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=10),
        ),
    ]
