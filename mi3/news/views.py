from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
# from django.views.generic import DetalView


def news_general(request):
    news = Articles.objects.all()
    return render(request, 'news/news.html', {'news': news})


def create(request):
    form = ArticlesForm()
    data = {
        'form': form,
    }
    return render (request, 'news/create.html', data)


# def create(request):
#     return render (request, 'news/create.html')