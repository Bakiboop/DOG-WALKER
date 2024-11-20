from django.shortcuts import render, redirect
from user_management.forms import UserSignUp , UserLogin
from django.contrib.auth import login , authenticate
from django.contrib import messages
# Create your views here.

def signup_view(request):
    
    if request.method=="POST":
        form = UserSignUp(request.POST or None)
        if form.is_valid():
            new_user =form.save()
            messages.success(request, "Account successfully created")
            new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request , new_user)
            return redirect("project:home")
    else:
        
        form = UserSignUp()
    
    context = {'form': form , }
    
    return render(request, 'signup.html' , context)

def login_view(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('project:home')  
    else:
        form = UserLogin()
    return render(request, 'login.html', {'form': form})



def home(request):
    return render(request, 'home.html')



    


