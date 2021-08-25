from django.urls import path

from backgroundapp.views import background_get, BackgroundDetailView, BackgroundListView

app_name = 'backgroundapp'

urlpatterns = [
    path('background_get/', background_get, name='background_get'),
    path('detail/<int:pk>', BackgroundDetailView.as_view(), name='detail'),
    path('list/', BackgroundListView.as_view(), name='list'),
]