# Generated by Django 3.2.8 on 2021-12-15 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_question_multi_sequence'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionnaire_item',
            options={'ordering': ['user', 'dicom', 'question__number']},
        ),
    ]