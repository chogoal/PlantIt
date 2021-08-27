from django.urls import path

from shopapp.views import PurchasingView

app_name = 'shopapp'

urlpatterns = [
    path('background/<int:background_pk>', PurchasingView.as_view(), name='backgroundpurchasing')
]
