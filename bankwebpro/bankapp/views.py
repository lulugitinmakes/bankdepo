from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from bankapp.forms import LoginForm, personform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
#home page
def home(request):
    return render(request,'home.html')

#loggin form
def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data['Username']
            pword=form.cleaned_data['Password']
            User=authenticate(request,username=uname,password=pword)
            if User is not None:
                login(request,User)
                return redirect('home')
            else:
                messages.info(request,'login failed')
                return redirect('log_new')
    else:
        form=LoginForm()
    return render(request,'loggin.html',{'form':form})


#register
def reg_ster(request):
    if request.method == 'POST':
       form=UserCreationForm()
       if form.is_valid():
           form.save()
           return redirect('in')
    else:
        form=UserCreationForm()
    return render(request,'registr.html',{'form':form})

#lognewpage
def lognew(request):
    return render(request, 'lognew.html')

#formpage

def formpage(request):
    if request.method=='POST':
        username=request.POST['Username']
        dateofbirth = request.POST['DOB']
        gender = request.POST['Gender']
        phonenum = request.POST['Phone']
        address = request.POST['Address']
        district = request.POST['District']
        acctype = request.POST['AccType']
        meterial1 = request.POST['Meterial']

        user=User.objects.create_user(Username=username,DOB=dateofbirth,Gender=gender,Phone=phonenum,Address=address,District=district,AccType=acctype,Meterial=meterial1)
        user.save()
        return redirect('home')

    return render(request,'form.html')

#Eranakulam dis
def ekm(request):
    return render(request,'ekm.html')

#kozhikode
def kozhikode(request):
    return render(request,'koz.html')

#malappuram
def mala(request):
    return render(request,'mala.html')

#wayanad
def waya(request):
    return render(request,'waya.html')

#kannur
def kannur(request):
    return render(request,'kannur.html')

#form2
def person_det(request):
    form = personform()
    if request.method == 'POST':
        form = personform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'accepted')
            return redirect('/form_new/')

    return render(request,'form2.html',{'form':form})

#form_new
def formnew(request):
    return render(request,'form_new.html')

#logout
def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')