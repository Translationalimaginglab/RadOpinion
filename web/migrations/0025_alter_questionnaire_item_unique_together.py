# Generated by Django 3.2.6 on 2021-08-14 20:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0024_alter_questionnaire_item_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='questionnaire_item',
            unique_together={('user', 'question', 'dicomFolder')},
        ),
    ]