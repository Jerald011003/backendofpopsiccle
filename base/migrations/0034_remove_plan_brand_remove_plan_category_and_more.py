# Generated by Django 4.1.7 on 2023-04-02 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_plan_createdat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='category',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='countInStock',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='createdAt',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='download',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='image',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='numReviews',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='numofPreorder',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='preorderdate',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='watch',
        ),
    ]
