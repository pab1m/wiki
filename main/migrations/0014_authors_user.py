# Generated by Django 4.2 on 2023-05-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='user',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]