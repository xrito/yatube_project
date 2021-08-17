from django.shortcuts import render
from django.http import HttpResponse

# Главная страница


def index(request):
    return HttpResponse('Главная страница')

# Страница с постами, отфилтрованные по группам


def group_posts(request, slug):
    return HttpResponse(f'Список групп {slug}')
