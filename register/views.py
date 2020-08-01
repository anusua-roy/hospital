from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import Admin

a = False

# Create your views here.
def register(request):
    global a
    if a:
        try:
            u = str(request.POST['username'])
            p1 = request.POST['pass1']
            p2 = request.POST['pass2']
            if p1 != p2:
                a = False
                messages.info(request, "Invalid Credentials.")
                return redirect("register")
            n = str(request.POST['name'])
            ad = str(request.POST['address'])
            d = request.POST['dob']
            s = request.POST['sex']
            c = request.POST['contact']
            e = request.POST['email']
            i = request.POST['image']
            user = Admin.objects.create(Username=u, Password=p1, Name=n, Image=i, Address=ad,
            DOB=d, Sex=s, Contact=c, Email=e)
        except:
            a = False
            messages.info(request, "Invalid Credentials.")
            return redirect("register")
        else:
            user.save()
            messages.info(request, "User Created Successfully!")
            return redirect("/")
    else:
        return render(request, 'register.html', {'a' : a})