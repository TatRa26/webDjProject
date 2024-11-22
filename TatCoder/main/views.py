from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def data(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")

def test(request):
    return HttpResponse("<h1>Это третья страница моего проекта на Django</h1>")

def test_view(request):
    # Ваша логика для отображения страницы
    return render(request, 'test.html')

