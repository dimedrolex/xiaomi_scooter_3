from django.shortcuts import render

def news_general(request):
    return render(request, 'news/news.html')
