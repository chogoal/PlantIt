from django.shortcuts import render

# Create your views here.


def gamepage(requests):
    return render(requests, 'gameapp/gamepage.html')


