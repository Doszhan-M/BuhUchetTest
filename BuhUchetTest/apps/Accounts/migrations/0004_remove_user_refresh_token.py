# Generated by Django 3.2.8 on 2021-10-29 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_user_refresh_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='refresh_token',
        ),
    ]
