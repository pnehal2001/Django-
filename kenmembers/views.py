from django.http import HttpResponse
from django.template import loader
from .models import Kenmem

def kenmembers(request):
    mymembers = Kenmem.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Kenmem.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request)) 
 
 
 
 
 
 




