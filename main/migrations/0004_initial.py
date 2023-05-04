# Generated by Django 4.2 on 2023-04-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_delete_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='ПІБ')),
                ('bio', models.TextField(verbose_name='Біографія')),
                ('photo', models.ImageField(upload_to='static/media')),
            ],
        ),
    ]
