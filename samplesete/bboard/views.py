from django.http import HttpResponse
from django.shortcuts import render

from bboard.models import Bb
from django.template import loader


# Create your views here.
def index(request):
    # s = f'Список объявлений' + '\r\n\r\n\r\n'
    #
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n' + str(bb.price) + '\r\n\r\n'
    # return HttpResponse(s, content_type='text / plain', charset='utf16')

    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
    context = {'bbs': bbs}
    # return HttpResponse(template.render(context, request))
    return render(request, 'bboard/index.html', context)
