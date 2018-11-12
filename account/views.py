from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_conf']:
            try:
                user= User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error':'Username already taken!'})
            except User.DoesNotExist:

                user = User.objects.create_user(request.POST['username'],  password=request.POST['password'])
                login(request, user)
                return render(request, 'account/signup.html')
        else:
            return render(request, 'account/signup.html', {'error':'Password didn\'t match!'})
    else:
        return render(request, 'account/signup.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'account/login.html', {'error':'Login Successful!!'})
        # Redirect to a success page.
        else:
        # Return an 'invalid login' error message.
            return render(request, 'account/login.html', {'error':'Authentication Error!'})
    else:
            return render(request, 'account/login.html')
