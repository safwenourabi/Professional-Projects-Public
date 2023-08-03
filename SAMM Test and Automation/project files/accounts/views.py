from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import accounts
from django.contrib import messages
from django import forms


# Create your views here.
var=""
def fn(username,password):
      for elem in  User.objects.all():
         print(elem.username,elem.password)
         if elem.username==username and elem.password==password :
             return elem 
      else:
          return None
def loginuser(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
       
        #user=fn(username,password)
        user = authenticate(username=username, password=password)
        print(user)
      
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('main')  
            #return redirect ('main/') 
        else :
            render(request,'s3.html')  
        

    return render(request,'s2.html')      
       
           
    

def signup(request):
    form = UserCreationForm(request.POST)
   

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid :
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            
           
            return(redirect('loginuser'))

    else:
        form = UserCreationForm()
       
        return render(request, 's.html',{'form':form})
      


def logoutuser(request):
    logout(request)
    return redirect('loginuser')