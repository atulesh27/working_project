from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegistration

# Create your views here.
def home(r):
    return HttpResponse('<h1> data from home page </h1>')

def showfromdata(request):
    form = StudentRegistration()
    return render(request,'app_form/userregistration.html',{'form':form})
