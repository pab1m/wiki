# Generated by Django 4.2 on 2023-04-27 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_task_authors_bio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Authors',
        ),
    ]
