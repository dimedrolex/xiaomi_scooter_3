from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_general, name='news_general'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail')
]
