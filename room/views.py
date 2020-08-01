from django.shortcuts import render
from home.models import Room

# Create your views here.
def room(request):
    try :
        i = request.POST['btn']
    except :
        i = 1
    finally :
        i = Room.objects.get(pk=i)
        r = Room.objects.all()
        return render(request, 'room.html', {'a': False, 'room' : r, 'i' :i})