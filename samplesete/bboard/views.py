from django.http import HttpResponse
from django.shortcuts import render

from bboard.models import Bb


# Create your views here.
def index(request):
    s = f'Список объявлений' + '\r\n\r\n\r\n'

    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n' + str(bb.price) + '\r\n\r\n'
    return HttpResponse(s, content_type='text / plain', charset='utf16')
