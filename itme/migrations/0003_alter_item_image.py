# Generated by Django 4.2.1 on 2023-05-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itme', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
    ]
