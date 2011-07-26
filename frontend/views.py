from django.template.response import TemplateResponse
from django.http import *

from frontend.utils import Hangul, Hanja

def home(request):
    text = request.GET.get('t', '')
    return TemplateResponse(request, 'home.html', {'text':text})
    
def translate(request):
    if 't' in request.GET:
        text = request.GET['t']
        result = Hanja.translate(text)

        return HttpResponse(result)
    else:
        return HttpResponseBadRequest('Invalid request')
