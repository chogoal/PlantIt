import random

from django.contrib.auth.models import User
from django.db.models import Count, Max
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from challengeapp.models import Challenge


def main_screen(request):
    return render(request, 'mainapp/main.html')


def get_random():
    chall_list = Challenge.CHALL_LIST
    r = random.randint(0, len(chall_list)-1)
    title = chall_list[r][1]
    challenge = Challenge(title=title)
    # 조건문 -> 만약 제목이 이미 db에 있으면 제외
    return challenge


class HomePageView(TemplateView):

    template_name = 'mainapp/home.html'

    def get_context_data(self, **kwargs):
        article_list = Article.objects.all().order_by('-like', '-created_at')

        context = super().get_context_data(**kwargs)
        context['best_articles'] = article_list[:8]
        context['random_challenge'] = get_random()

        return context


