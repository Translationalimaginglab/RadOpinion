from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def fuck(request):
    return render(request, 'sample.html', )
