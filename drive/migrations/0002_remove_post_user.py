# Generated by Django 4.0.6 on 2022-07-17 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]