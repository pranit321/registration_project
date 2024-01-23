from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def registration(request):
    usfo=UserForm()
    pfo=ProfileForm()
    d={'usfo':usfo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            MUFDO.set_password(ufd.cleaned_data['password'])
            MUFDO.save()
            MPFD=pfd.save(commit=False)
            MPFD.Usernames=MUFDO
            MPFD.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not')


    return render(request,'registration_form.html',d)