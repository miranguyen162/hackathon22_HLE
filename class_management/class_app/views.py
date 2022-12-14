from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from class_app.forms import SignUpForm

def frontpage(request):
    return render(request, 'frontpage.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        
    return render(request, 'login.html', {})


