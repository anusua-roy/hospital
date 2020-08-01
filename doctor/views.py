from django.shortcuts import render
from home.models import Department

# Create your views here.
def doctor(request):
    try :
        i = request.POST['btn']
    except :
        i = 1
    finally :
        i = Department.objects.get(pk=i)
        dept = Department.objects.all()
        return render(request, 'doctor_list.html', {'a': False, 'dept' : dept, 'i': i})