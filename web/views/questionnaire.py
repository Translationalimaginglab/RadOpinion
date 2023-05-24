from ..models import *
from . import login
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
import os, re, copy


class QuestionnaireView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        print('=====QuestionnaireView-get=====')
        user = login.LoginView.get_user(request)
        if not user:
            return redirect('login')
        # moved from login:
        QuestionnaireContext.create_questionnaire(user)
        #
        q_item = self.fetch_q_item(user=user, dicom=None, command='last-answered')
        data = QuestionnaireContext(q_item).as_dict
        print(data)
        return render(request, 'questionnaire.html', context={'data': data}, )

    def post(self, request: HttpRequest) -> HttpResponse:
        print('=====QuestionnaireView-post=====')
        user = login.LoginView.get_user(request)
        if not user:
            return redirect('login')
        q_item = self.fetch_q_item(
            user, request.POST['dicom'], request.POST['command'])
        if request.POST['command'] == 'first-unanswered' and q_item is None:
            return render(request, 'thanks.html',
                          context={'user': login.LoginView.display_name(user)}, )
        elif q_item is None:
            return redirect('questionnaire')
        else:
            zoom = request.session['zoom'] if 'zoom' in request.session else 100
            data = QuestionnaireContext(q_item, zoom).as_dict
            return render(request, 'questionnaire.html', context={'data': data}, )

    def fetch_q_item(self, user, dicom, command) -> QuestionnaireItem:
        print('=====fetch_q_item=====')
        print(user.username, dicom, command)
        match command:
            case 'first':
                q_item = QuestionnaireItem.objects.filter(user=user).first()
            case 'previous':
                q_item = QuestionnaireItem.objects.filter(user=user, dicom__lt=dicom).last()
            case 'next':
                q_item = QuestionnaireItem.objects.filter(user=user, dicom__gt=dicom).first()
            case 'first-unanswered':
                q_item = QuestionnaireItem.objects.filter(user=user, answer=None).first()
            case 'last-answered':
                q_item = QuestionnaireItem.objects.filter(user=user).exclude(answer=None).last()
                q_item = q_item if q_item else self.fetch_q_item(user, dicom, 'first')
            case _:
                q_item = None
        return q_item


class QuestionnaireContext:
    user = None
    q_item = {}
    dicomSequences = []
    n_all = 0
    n_answered = 0
    order = ''
    zoom = 100

    def __init__(self, q_item, zoom=100):
        self.user = login.LoginView.display_name(q_item.user)
        self.q_item = copy.copy(vars(q_item))
        self.q_item.pop('_state')
        self.q_item['question'] = vars(q_item.question)
        self.q_item['question'].pop('_state')
        choices = Choice.objects.filter(
            question=q_item.question).values_list('text', flat=True)
        self.q_item['question']['choices'] = list(choices)
        self.dicomSequences = self.dicom_sequences(
            q_item.dicom, q_item.question.multi_sequence)
        self.n_all = QuestionnaireItem.objects.filter(user=q_item.user).count()
        self.n_answered = QuestionnaireItem.objects.filter(user=q_item.user) \
            .exclude(answer=None).count()
        self.order = 'first' if q_item == QuestionnaireItem.objects.filter(user=q_item.user).first() \
            else 'last' if q_item == QuestionnaireItem.objects.filter(user=q_item.user).last() \
            else 'mediate'
        self.zoom = zoom

    @property
    def as_dict(self):
        return vars(self)

    BASE_PATH = './web/static/dicom-data/'
    BASE_URL = '/static/dicom-data/'

    @staticmethod
    def dicom_sequences(dicom_name: str, multi: bool) -> list[dict]:
        print('=========dicom_sequences========')
        dicom_path = QuestionnaireContext.BASE_PATH + dicom_name
        dicom_url = QuestionnaireContext.BASE_URL + dicom_name
        sequenceFolder_list = [folder for folder in os.listdir(dicom_path)
                               if os.path.isdir(dicom_path + '/' + folder)]
        sequence_list = []
        for sequenceFolder in sequenceFolder_list:
            # sequenceName = re.sub(r'^\d+[-.] *', '', sequenceFolder)
            sequence_path = dicom_path + '/' + sequenceFolder + '/'
            sequence_url = dicom_url + '/' + sequenceFolder + '/'
            sequence_files = [sequence_url + file for file in os.listdir(sequence_path)
                              if os.path.isfile(sequence_path + file) and re.search('.dcm$', file)]
            sequence_list.append(
                {'name': sequenceFolder, 'files': ' | '.join(sequence_files)})
            if not multi:
                break
        return sequence_list

    @staticmethod
    def create_questionnaire(user: User) -> None:
        base_path = QuestionnaireContext.BASE_PATH
        dicomFolder_list = [folder for folder in os.listdir(base_path)
                            if os.path.isdir(base_path + folder)]
        question_list = Question.objects.all()
        tobedeleted = QuestionnaireItem.objects.filter(user=user)
        for dicom in dicomFolder_list:
            tobedeleted = tobedeleted.exclude(dicom=dicom)
        tobedeleted.delete()
        for folder in dicomFolder_list:
            for q in question_list:
                QuestionnaireItem.objects.get_or_create(
                    user=user, question=q, dicom=folder)
