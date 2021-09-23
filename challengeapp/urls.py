from django.urls import path

from challengeapp.views import ChallengeCreateView, ChallengeDetailView, ChallengeUpdateView, ChallengeDeleteView, \
    ChallengeListView

app_name = 'challengeapp'

urlpatterns = [
    path('list/', ChallengeListView.as_view(), name='list'),
    path('create/', ChallengeCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ChallengeDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ChallengeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ChallengeDeleteView.as_view(), name='delete'),
]