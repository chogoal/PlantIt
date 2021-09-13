from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from challengeapp.models import Challenge


def main_screen(request):
    return render(request, 'mainapp/main.html')


class HomePageView(TemplateView):

    template_name = 'mainapp/home.html'

    def get_context_data(self, **kwargs):
        article_list = Article.objects.annotate(like_count=Count('like')).order_by('-like_count', '-created_at')
        challenge_list = Challenge.objects.filter(success=False)

        context = super().get_context_data(**kwargs)
        context['best_articles'] = article_list[:10]
        context['challenge_list'] = challenge_list[:10]

        return context


