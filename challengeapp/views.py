import random

from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from challengeapp.forms import ChallengeCreationForm
from challengeapp.models import Challenge


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ChallengeCreateView(CreateView):
    model = Challenge
    form_class = ChallengeCreationForm
    template_name = 'challengeapp/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


class ChallengeDetailView(DetailView):
    model = Challenge
    context_object_name = 'target_challenge'
    template_name = 'challengeapp/detail.html'


class ChallengeUpdateView(UpdateView):
    model = Challenge
    form_class = ChallengeCreationForm
    context_object_name = 'target_challenge'
    template_name = 'challengeapp/update.html'

    def get_success_url(self):
        return reverse('challengeapp:detail', kwargs={'pk': self.object.pk})


class ChallengeDeleteView(DeleteView):
    model = Challenge
    context_object_name = 'target_challenge'
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'challengeapp/delete.html'


class ChallengeListView(ListView):
    model = Challenge
    context_object_name = 'challenge_list'
    template_name = 'challengeapp/list.html'
    paginate_by = 5

