# Generated by Django 3.2.6 on 2021-08-11 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dicom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]