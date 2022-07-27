from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def news_general(request):
    news = Articles.objects.all()
    return render(request, 'news/news.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details.html'
    context_object_name = 'article_gen'


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'

    form = ArticlesForm()

    data = {
        'form': form,
        # 'error': error
    }
    return render (request, 'news/create.html', data)


# def create(request):
#     return render (request, 'news/create.html')