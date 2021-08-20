from django.shortcuts import render

# Create your views here.


def main_screen(request):
    return render(request, 'mainapp/main.html')


def home(request):
    return render(request, 'mainapp/home.html')

