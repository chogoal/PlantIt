from django.urls import path

from gameapp.views import gamepage

app_name = 'gameapp'

urlpatterns = [
    path('game/', gamepage, name='game'),
]