from.models import*
from.forms import Loginform,Signupform
from django.shortcuts import render,redirect

def Signup(request):
    form = Signupform
    return render(request,'accounts/signup.html',{'form':form})
def Login(request):
    form = Loginform    
    return render(request,'accounts/login.html',{'form':form})
    