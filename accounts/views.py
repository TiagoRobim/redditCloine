from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_conf']:
            try:
                user= User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username already taken!'})
            except User.DoesNotExist:

                user = User.objects.create_user(request.POST['username'],  password=request.POST['password'])
                login(request, user)
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error':'Password didn\'t match!'})
    else:
        return render(request, 'accounts/signup.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST and request.POST['next'] is not None:
                return redirect(request.POST['next'])
            return redirect('home')
        # Redirect to a success page.
        else:
        # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html', {'error':'Authentication Error!'})
    else:
            return render(request, 'accounts/login.html')

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
