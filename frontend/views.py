from django.template.response import TemplateResponse
from django.http import *

from frontend.utils import Hangul, Hanja

def home(request):
    text = request.GET.get('t', '')
    return TemplateResponse(request, 'home.html', {'text':text})
    
def translate(request):
    if 't' in request.GET:
    	mode = request.GET['m']
        text = request.GET['t']
        result = Hanja.translate(text, mode)

        return HttpResponse(result)
    else:
        return HttpResponseBadRequest('Invalid request')
