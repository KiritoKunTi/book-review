# Generated by Django 4.0.4 on 2022-05-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitap', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
