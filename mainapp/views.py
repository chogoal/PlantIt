from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from articleapp.models import Article


def main_screen(request):
    return render(request, 'mainapp/main.html')


def home(request):
    return render(request, 'mainapp/home.html')


class HomePageView(TemplateView):

    template_name = 'mainapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context


