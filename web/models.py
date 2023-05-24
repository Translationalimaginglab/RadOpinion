from django.db import models
from django.contrib.auth.models import User
import random, uuid


class Question(models.Model):
    number = models.FloatField(unique=True, null=True)
    text = models.CharField(max_length=1000)
    type = models.CharField(max_length=15, default='one', choices=[(
        'multiple', '1 of n choices'), ('ture/false', 'True/False'), ('descriptive', 'Descriptive')])
    multi_sequence = models.BooleanField(default=False, null=False)
    drawable_sequence = models.IntegerField(default=0, null=False)

    class Meta:
        ordering = ['number', ]

    def __str__(self):
        return '[{}] {}. {}'.format(self.type, int(self.number) if self.number.is_integer() else self.number,
                                    self.text[:70] + '...' if len(self.text) > 75 else self.text)


class Choice(models.Model):
    letter = models.CharField(max_length=1, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    class Meta:
        unique_together = ['question', 'letter']
        ordering = ['question', 'letter']

    def __str__(self):
        return 'Question({}): {}. {}'.format(self.question.number, self.letter, self.text)


def randomFloat():
    return random.random()


class QuestionnaireItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dicom = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000, null=True)
    rand = models.FloatField(default=randomFloat)
    drawing_state = models.CharField(max_length=10000, null=True)

    class Meta:
        unique_together = ['user', 'dicom', 'question', ]
        ordering = ['user', 'dicom', 'question__number']

    def __str__(self):
        return 'User({}), {}, Question({}): {}'.format(self.user, self.dicom, self.question.number, self.answer)


def randomToken():
    return uuid.uuid4()


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=randomToken, null=False)

    def __str__(self):
        return '{}_token'.format(self.user)
