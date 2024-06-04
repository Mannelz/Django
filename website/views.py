from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, 'home.html', {'records':records})
    else:
        return redirect('login')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao efetuar o login! Tente novamente.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.error(request, 'Você precisa estar logado para acessar esta página!')
        return redirect('login')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Cliente adicionado com sucesso!')
                return redirect('home')
        else:
            return render(request, 'add_record.html', {'form':form})
    else:
        messages.error(request, 'Você precisa estar logado para adicionar um cliente!')
        return redirect('login')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Cliente deletado com sucesso!')
        return redirect('home')
    else:
        messages.error(request, 'Você precisa estar logado para deletar um cliente!')
        return redirect('login')