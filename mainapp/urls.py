from django.urls import path

from mainapp.views import main_screen, home

app_name = 'mainapp'

urlpatterns = [
    path('', main_screen, name='main_screen'),
    path('home/', home, name='home')
]