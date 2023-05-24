from ..models import *
from . import login, questionnaire
from django.views import View
from django.http import HttpRequest, JsonResponse


class AjaxView(View):

    def post(self, request: HttpRequest) -> JsonResponse:
        print('=====AjaxView-post=====')
        # time.sleep(1)
        json_response = {'login_required': False, 'reload_required': False,
                         'error_message': None, 'data': None, }

        user = login.LoginView.get_user(request)
        if not user:
            json_response['login_required'] = True
            json_response['error_message'] = 'Session has expired.'
            return JsonResponse(json_response)

        request.session['zoom'] = request.POST['zoom']
        answer = request.POST['answer'] if 'answer' in request.POST else None
        if not self.save_answer(user, request.POST['dicom'], request.POST['question_number'],
                                answer, request.POST['drawing_state'], ):
            json_response['login_required'] = True
            json_response['error_message'] = 'Answer not saved.'
            return JsonResponse(json_response)

        q_item = self.get_questionnaire_item(
            user, request.POST['dicom'], request.POST['question_number'], request.POST['command'])
        if q_item is None:
            json_response['reload_required'] = True
            json_response['error_message'] = 'Dicom/question.multi has changed.'
            print('ajax error:', json_response['error_message'])
            return JsonResponse(json_response)

        json_response['data'] = questionnaire.QuestionnaireContext(q_item, request.session['zoom']).as_dict
        print(json_response)
        return JsonResponse(json_response)

    @staticmethod
    def get_questionnaire_item(user: User, dicom, question_number, command) \
            -> QuestionnaireItem | None:
        match command:
            case 'previous':
                q_item = QuestionnaireItem.objects.filter(
                    user=user, dicom=dicom, question__number__lt=question_number).last()
            case 'next':
                q_item = QuestionnaireItem.objects.filter(
                    user=user, dicom=dicom, question__number__gt=question_number).first()
            case 'first-unanswered':
                q_item = QuestionnaireItem.objects.filter(
                    user=user, answer=None).order_by('dicom', 'question__number').first()
            case _:
                q_item = None
        if q_item is None or q_item.dicom != dicom or \
                q_item.question.multi_sequence != Question.objects.get(number=question_number).multi_sequence:
            return None
        else:
            return q_item

    @staticmethod
    def save_answer(user, dicom, question_number, answer, drawing_state):
        print('=====AjaxView-save-answer=====')
        print('save:', user, question_number, dicom, answer)
        q_item = QuestionnaireItem.objects.get(
            user=user, question__number=question_number, dicom=dicom)
        q_item.answer = None if answer == '' else answer
        q_item.drawing_state = None if drawing_state == '' else drawing_state
        q_item.save()
        return True