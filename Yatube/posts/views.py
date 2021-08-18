from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Главная страница
def index(request):
    return render(request, 'posts/index.html')

def group_list(request):
    return render(request, 'posts/group_list.html')    

# Страница с постами, отфилтрованные по группам
def group_posts(request, slug):
    return HttpResponse(f'Список групп {slug}')
