# Generated by Django 3.2.8 on 2021-10-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_user_refresh_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True),
        ),
    ]
