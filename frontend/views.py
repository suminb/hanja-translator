from django.template.response import TemplateResponse
from django.http import *

from dict import *

def home(request):
    return TemplateResponse(request, 'home.html', {})
    
def translate(request):
    if 'q' in request.GET:
        query = request.GET['q']
        result = ''.join(map(lambda x: table[x] if x in table else x, query))

        return HttpResponse(result)
    else:
        return HttpResponseBadRequest('Invalid request')
