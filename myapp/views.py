# --------- View.py ---------
from django.shortcuts import render,redirect
from .form import UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import LinksUser
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' # email validation using regex 
def SigninView(request):
  form = UserLoginForm()
  if request.method == 'POST':
      email_or_uname = request.POST.get('email_or_uname')
      upass = request.POST.get('password')
      if re.fullmatch(regex, email_or_uname): # with email authenticate
        get_user = LinksUser.objects.filter(email=email_or_uname)
        if not len(get_user) == 0:
        
          user = authenticate(username=get_user[0].username,password=upass)
          print(get_user[0].username)
          print(upass)
          print(user)
          if user is None:
              messages.error(request,'Please Enter Correct Credinatial')
              return redirect('/')
          else:
              login(request,user)
              messages.success(request,'Login Successful')
          return redirect('/dash/')
        else:
          print('Invalid Credential !')
          return redirect('/')
      else:# authenticatewith using  
        user = authenticate(username=email_or_uname,password=upass)
        print(user)
        if user is None:
            messages.error(request,'Please Enter Correct Credinatial')
            return redirect('/')
        else:
            login(request,user)
            messages.success(request,'Login Successful')
        return redirect('/dash/')
  else:
      if request.user.is_authenticated:
          return redirect('/dash/')
      else:
          return render(request,'index.html',{'form':form})
      
def DashView(request):
    
  return render(request,'dash.html')

def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'You are Successfully Logged Out !')
        return redirect('/')
    else:
        messages.info(request, 'Please Login First')
    return redirect('/')