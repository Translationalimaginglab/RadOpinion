from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginView(View):
    error_message = None

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, 'login.html', context={'error': LoginView.error_message}, )

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user:
            request.session['user.username'] = user.username
            # user_token, created = Token.objects.get_or_create(user=user)
            # questionnaire.QuestionnaireContext.create_questionnaire(user)
            return redirect('questionnaire')
        else:
            LoginView.error_message = 'Incorrect username or password!\nNote that both fields are case-sensitive.'
            return redirect('login')

    @staticmethod
    def get_user(request: HttpRequest) -> User:
        if User.objects.filter(username=request.session['user.username']).exists():
            return User.objects.get(username=request.session['user.username'])
        else:
            LoginView.error_message = 'Your session is expired.\nPlease log-in again.'
            return None

    @staticmethod
    def display_name(user: User) -> str:
        return user.first_name if user.first_name and user.first_name != '' \
            else user.username


class LogoutView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        request.session['user.username'] = None
        LoginView.error_message = 'You\'ve been logged out. Log in again.'
        return redirect('login')
