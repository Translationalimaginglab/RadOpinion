from web.models import *
from django.views import View
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import csv


class ReportView(View):
    username = None

    def get(self, request: HttpRequest, username: str = None) -> HttpResponse:
        if username:
            self.username = username
            return self.csv_response
        else:
            return render(request, 'report.html', context={'users': self.user_list}, )

    @property
    def user_list(self) -> list[str]:
        users = QuestionnaireItem.objects.exclude(user=None).values_list(
            'user__username', flat=True).distinct().order_by()
        return list(users)

    @property
    def csv_response(self) -> HttpResponse:
        csv_response = HttpResponse(content_type='text/csv', headers={
            'Content-Disposition': 'attachment; filename="{}.csv"'.format(self.username)}, )
        csv_writer = csv.writer(csv_response)

        q_items = QuestionnaireItem.objects.filter(
            user__username=self.username).order_by('question__number')
        q_dicom_list = q_items.values_list(
            'dicom', flat=True).distinct().order_by('dicom')
        csv_writer.writerow([' ', ' '] + [' ' + dicom for dicom in q_dicom_list])

        q_question_list = q_items.values_list(
            'question', flat=True).distinct().order_by('question__number')
        for question_id in q_question_list:
            q = Question.objects.get(id=question_id)
            answers = [q_items.get(question__id=question_id, dicom=dicom).answer
                       for dicom in q_dicom_list]
            row = [int(q.number) if q.number.is_integer() else q.number, q.text] + \
                  [answer if answer else '-' for answer in answers]
            csv_writer.writerow(row)

        return csv_response
