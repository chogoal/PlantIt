from django.forms import ModelForm

from challengeapp.models import Challenge


class ChallengeCreationForm(ModelForm):
    class Meta:
        model = Challenge
        fields = ['title', 'image', 'content']
