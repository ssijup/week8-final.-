# Generated by Django 4.1.5 on 2023-02-11 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_products_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(upload_to='productimg'),
        ),
    ]