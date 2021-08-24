from django.urls import path

from mainapp.views import main_screen, home, HomePageView

app_name = 'mainapp'

urlpatterns = [
    path('', main_screen, name='main_screen'),
    path('home/', HomePageView.as_view(), name='home')
]