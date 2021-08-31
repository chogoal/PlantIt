from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView

from backgroundapp.models import Background
from shopapp.models import Purchasing


class PurchasingView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        background = Background.objects.get(pk=kwargs['background_pk'])

        purchase_record = Purchasing.objects.filter(user=user, background=background)

        try:
            if purchase_record.exists():
                raise overlapException('이미 있음')

            elif user.profile.mileage >= background.price:
                purchase = Purchasing(user=user, background=background)
                messages.add_message(request, messages.SUCCESS, 'user.profile.mileage')
                user.profile.mileage -= background.price
                background.state = 'sold'
                purchase.save()
                user.profile.save()
                background.save()

            else:
                raise lackException('잔고 부족')

        except lackException:
            messages.add_message(request, messages.ERROR, '잔고가 부족해요')
            return HttpResponseRedirect(reverse('backgroundapp:detail',
                                                kwargs={'pk': kwargs['background_pk']}))
        except overlapException:
            messages.add_message(request, messages.ERROR, '이미 삼')
            return HttpResponseRedirect(reverse('backgroundapp:detail',
                                                kwargs={'pk': kwargs['background_pk']}))

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('backgroundapp:detail', kwargs={'pk': kwargs['background_pk']})


class lackException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class overlapException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
