# Generated by Django 4.1.7 on 2023-03-31 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_alter_product_download'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='download',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
