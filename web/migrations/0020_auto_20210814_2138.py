# Generated by Django 3.2.6 on 2021-08-14 17:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_token_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='token',
        ),
        migrations.AddField(
            model_name='token',
            name='tokenn',
            field=models.UUIDField(default=uuid.UUID('3f7509e3-9657-4b23-acf1-bc7a460a7601')),
        ),
    ]
