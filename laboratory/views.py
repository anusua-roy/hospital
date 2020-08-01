from django.shortcuts import render
from home.models import Laboratory

# Create your views here.
def laboratory(request):
    try :
        i = request.POST['btn']
    except :
        i = 1
    finally :
        i = Laboratory.objects.get(pk=i)
        l = Laboratory.objects.all()
        return render(request, 'laboratory.html', {'a': False, 'lab' : l, 'i' :i})