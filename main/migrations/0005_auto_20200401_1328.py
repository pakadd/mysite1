# Generated by Django 2.2 on 2020-04-01 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200401_1256'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bbmain',
            new_name='Bb',
        ),
        migrations.RenameField(
            model_name='bb',
            old_name='autor',
            new_name='author',
        ),
    ]
