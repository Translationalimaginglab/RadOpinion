from django.urls import path
from .views import login, report, question_list, questionnaire, ajax, sample

urlpatterns = [
    path('login/', login.LoginView.as_view(), name='login'),
    path('logout/', login.LogoutView.as_view(), ),
    path('question-list/', question_list.QuestionsView.as_view(), ),
    path('report/', report.ReportView.as_view(), ),
    path('report/<str:username>/', report.ReportView.as_view()),

    path('questionnaire/', questionnaire.QuestionnaireView.as_view(),
         name='questionnaire'),
    path('ajax/', ajax.AjaxView.as_view(), ),

    path('sample/', sample.fuck, ),

]
