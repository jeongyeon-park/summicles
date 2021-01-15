from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Article
# Create your views here.


class ArticleList(ListView):
    model = Article
    template_name = 'main_page.html'
    context_object_name = 'main_page'
