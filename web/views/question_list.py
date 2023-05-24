from ..models import *
from django.views import View
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


class QuestionsView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'questions.html', context={'questions': self.question_list}, )

    @property
    def question_list(self) -> list[dict]:
        questions = []
        for q in Question.objects.order_by('number').all():
            choices = Choice.objects.filter(question=q).values_list('text', flat=True)
            question = {'number': q.number if not q.number.is_integer() else int(q.number),
                        'type': q.type, 'text': q.text, 'choices': list(choices), }
            questions.append(question)
        return questions
