# Generated by Django 3.2.6 on 2021-08-14 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_alter_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.UUIDField(default=uuid.UUID('f05509aa-d703-4e34-88e5-5cd52cc9553f')),
        ),
    ]