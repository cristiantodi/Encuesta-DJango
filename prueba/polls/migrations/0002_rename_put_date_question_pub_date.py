# Generated by Django 3.2.9 on 2021-11-18 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='put_date',
            new_name='pub_date',
        ),
    ]
