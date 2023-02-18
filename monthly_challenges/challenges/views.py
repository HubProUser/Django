from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Eat no unhealthy food for 1 month'
    elif month == 'february':
        challenge_text = 'Work for at least 20 minutes every day'
    elif month == 'march':
        challenge_text = 'Try doing some work'
    else:
        return HttpResponseNotFound('This month is not supported.')
    return HttpResponse(challenge_text)
