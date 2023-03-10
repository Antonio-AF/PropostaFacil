from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Rota para a Página inicial
def modelo(request):
    return render(request, 'modelo.html')


# Rota para a tela de login
def painel(request):
    return render(request, 'painel.html')


# Rota de processamento do Login
def dologin(request):
    data = {}

    name = request.POST["username"]
    pswd = request.POST["password"]
    user = authenticate(request, username=name, password=pswd)

    if user:
        print("Valid user " + str(user))
        login(request, user)
        return redirect('/proposta/')
    else:
        data['msg'] = 'Usuário ou Senha Inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'login_form.html', data)


# Rota para a página de cadastro onde está o formulário de cadastro de novos usuários.
def signup(request):
    return render(request, 'signup.html')


# Rota de inserção dos dados do usuário no Banco de Dados.
def store(request):
    data = {}

    if request.POST['password'] != request.POST['password-conf']:

        data['msg'] = 'Senha não Conferem!'
        data['class'] = 'alert-danger'

    else:

        username = request.POST["username"]
        email = None
        password = request.POST["password"]

        user = User.objects.create_superuser(username=username, email=email, password=password)

        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'

    return render(request, 'signup.html', data)


def proposta(request):
    return render(request, 'proposta.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def login_form(request):
    return render(request, 'login_form.html')


def cadastro(request):
    return render(request, 'cadastro.html')


