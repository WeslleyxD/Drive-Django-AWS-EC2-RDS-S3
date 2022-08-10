from django.shortcuts import render, redirect
from drive.forms import LoginForm, RegisterForm, UploadForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from s3.login import login_aws
from s3.requests import link_open_item, delete_item_user, validate_limit_storage, upload_file


# Create your views here.
@login_required
def dashboard(request, user):
    return render(request, 'dashboard.html', {})

def upload(request):
    s3 = login_aws()  
    if request.method == 'POST':
        upload_form = UploadForm(data=request.POST, files=request.FILES)
        if upload_form.is_valid():
            cd = upload_form.cleaned_data
            file = cd['file']
            validate = validate_limit_storage(user=request.user, file=file.size)
            if validate == True:
                upload_file(file, f'{request.user}/{file}')
                messages.success(request, 'Arquivo salvo com sucesso')
                return redirect('drive:dashboard',  user=request.user)
            else:
                messages.error(request, 'Limite de armazenamento excedido')
                return redirect('drive:dashboard',  user=request.user)

        return render(request, 'upload.html', {'upload_form' : upload_form})
    else:
        upload_form = UploadForm()
    return render(request, 'upload.html', {'upload_form' : upload_form})

def delete_item(request, item):
    if request.method == 'POST':
        item = str(item)
        delete_item_user(key=f'{request.user}/{item}')
        return redirect('drive:dashboard', user=request.user)
    else:
        return render(request, 'delete_item.html', {'item': item})

def test(request):
    return render(request, 'test.html')


#######################3 AUTHENTICATE #######################3
def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'login_done.html' ,{})
                else:
                    return HttpResponse('Disabled account')
            else:
                messages.error(request, 'Invalid login')
                return redirect ('drive:login')
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form' : login_form})

def user_register(request):
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            if User.objects.filter(username=cd['username']):
                messages.error(request, 'Usuario ja existe')
                return render(request, 'register.html', {'register_form': register_form})
            else:
                new_user = User.objects.create_user(username=cd['username'], password=cd['password'])
                new_user.save()
                messages.success(request, 'Usuário criado com sucesso, faça o login para continuar')
                return redirect('drive:login')
        else:
            messages.error(request, 'Usuário já existe!')
    else:
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

def user_logout(request):
    logout(request)
    return redirect ('drive:login')





# TODO: Completar o CRUD no delete excluir a pasta do user do bucket igual ao model Foreign Key on_delete=models.CASCADE.