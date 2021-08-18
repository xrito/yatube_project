from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
    }
    return render(request,  template, context)


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return render(request,  template, context)


def group_posts(request, slug):
    return HttpResponse(f'Список групп {slug}')