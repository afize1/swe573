from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserChangePasswordForm, ChangePasswordForm
from .models import users
from django.contrib.auth.models import User   ##save details about user such as sequrity question
from django.contrib.auth.hashers import make_password ##save password encrypted


def index(request):
    return render(request, 'user/index.html',{'title':'index'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            email1 = request.POST.get('email')
            email2= request.POST.get('verify_email')
            if email1 != email2:
                messages.info(request, f'Mail adresses are not matched, please check!')
            else:
                username = request.POST.get('username')
                form.save()
                username = form.cleaned_data.get('username')
                en=users(username=request.POST.get('username'),security_question=request.POST.get('security_question'),answer=request.POST.get('answer'))
                en.save()
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form,'title':'reqister here'})

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' Welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'Account does not exist, please sign in!')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form,'title':'log in'})


def forgotPassword(request):
    if request.method == 'POST':
        form = UserChangePasswordForm(request.POST) or None
        if form.is_valid():
            username = request.POST.get('username')
            security_question = request.POST.get('security_question')
            answer = request.POST.get('answer')
            user = users.objects.filter(username=username)
            if user is not None:
                valid_security_question = user[0].security_question
                valid_answer = user[0].answer
                if security_question==valid_security_question:
                    if answer==valid_answer:
                        return redirect('setPassword',username)
                    else:
                        messages.info(request, f'answer is wrong')
                else:
                    messages.info(request, f'security question is wrong')
            else:
                messages.info(request, f'account does not exit plz sign in')
    else:
        form = UserChangePasswordForm()
    return render(request, 'user/forgotPassword.html', {'form': form,'title':'reqister here'})

def setPassword(request, username):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST) or None
        password1 = request.POST.get('new_password1')
        password2 = request.POST.get('new_password2')
        if password1==password2:
            user = User.objects.filter(username=username)
            password = make_password(password1)
            user.update(password=password)
            messages.success(request, f'Your password has been changed! You are now able to log in')
            return redirect('login')
        else:
            messages.success(request, f'Your password has not been changed!')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'user/setPassword.html', {'form': form,'title':'reqister here'})