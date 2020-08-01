from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import *
from datetime import date

a = False
pos = ''

# Create your views here.
def home(request):
    global a
    a = False
    return render(request, 'login.html', {'a': a})

def user(request):
    global a
    global pos
    if a:
        return render(request, 'home.html', {'a': a, 'pos' : pos})
    else:
        try:
            user = str(request.POST['uname'])
            psw = request.POST['psw']
            pos = str(request.POST['position'])
            if pos == 'admin':
                a = Admin.objects.get(Username=user, Password=psw)
            elif pos == 'doctor':
                a = Doctor.objects.get(Username=user, Password=psw)
            elif pos == 'patient':
                a = Patient.objects.get(Username=user, Password=psw)
        except:
            a = False
            messages.info(request, "Invalid Credentials")
            return redirect("/")
        else:
            return render(request, 'home.html', {'a': a, 'pos' : pos})

def roomlist(request):
    global a
    try :
        i = request.POST['btn']
    except :
        i = 1
    finally :
        i = Room.objects.get(pk=i)
        r = Room.objects.all()
        return render(request, 'room.html', {'a': a, 'room' : r, 'i' :i})

def lablist(request):
    global a
    try :
        i = request.POST['btn']
    except :
        i = 1
    finally :
        i = Laboratory.objects.get(pk=i)
        l = Laboratory.objects.all()
        return render(request, 'laboratory.html', {'a': a, 'lab' : l, 'i' :i})

def doclist(request):
    global a
    try :
        i = request.POST['btn']
    except :
        i = 1
    finally :
        i = Department.objects.get(pk=i)
        dept = Department.objects.all()
        return render(request, 'doctor_list.html', {'a': a, 'dept' : dept, 'i': i})

def patientlist(request):
    global a
    global pos
    if pos == 'admin':
        pat = Patient.objects.all()
    elif pos == 'doctor':
        pat = a.patient_set.all()
    return render(request, 'patient_list.html', {'a': a, 'pat' : pat, 'pos' : pos})

def profile(request):
    global a
    return render(request, 'profile.html', {'a' : a})

def bill(request):
    global a
    global pos
    if pos == 'doctor':
        id = int(request.POST['btn'])
        p = Patient.objects.get(pk=id)
        return render(request, 'generate_bill.html', {'a': a, 'p' : p, 'pos' : pos})
    else:
        if pos == 'patient':
            p = a
        elif pos == 'admin':
            id = int(request.POST['btn'])
            p = Patient.objects.get(pk=id)
        
        #other charges
        d = date.today() - p.DOJ
        d = int(d.days)
        hc = d*200
        rc = d*int(p.BID.RID.Fees)
        dc = d*int(p.DID.Fees)

        #report charges
        r = p.report_set.all()
        trp = 0
        for i in r:
            trp+=int(i.LID.Fees)
        
        #total charges
        total = hc+rc+dc+trp

        return render(request, 'generate_bill.html', {'a': a, 'p' : p, 'pos' : pos, 'days': d, 'hos' : hc, 'room':rc, 'doc': dc, 'trp': trp, 'total': total})