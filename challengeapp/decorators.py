from django.http import HttpResponseForbidden

from challengeapp.models import Challenge


def challenge_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_challenge = Challenge.objects.get(pk=kwargs['pk'])
        if target_challenge.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated