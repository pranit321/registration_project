from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *

def registration(request):
    usfo=UserForm()
    pfo=ProfileForm()
    d={'usfo':usfo,'pfo':pfo}
    return render(request,'registration_form.html',d)