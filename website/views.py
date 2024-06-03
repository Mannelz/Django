from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'post':
        username = request.post['username']
        password = request.post['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('home')
        else:
            messages.success(request, 'Erro ao efetuar o login! Tente novamente.')
            return redirect('login')
    else:
        return render('login')

def logout_user(request):
    pass