# Generated by Django 4.2 on 2023-04-28 12:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_authors_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='photo',
            field=models.ImageField(blank=True, height_field=500, null=True, upload_to='authors_img', validators=[django.core.validators.validate_image_file_extension], width_field=500),
        ),
    ]