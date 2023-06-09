# Generated by Django 3.2.6 on 2021-08-09 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20210809_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together={('question', 'number')},
        ),
    ]
