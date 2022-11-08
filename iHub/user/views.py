from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserChangePasswordForm, ChangePasswordForm
from .models import users



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
            try:
                password_user = users.objects.get(username)
            except:
                messages.success(request, f'User does not exist')
                return redirect('forgotPassword')
            
            valid_answer = password_user.answer
            valid_security_question = password_user.security_question
            if security_question == valid_security_question:
                if answer == valid_answer:
                    return redirect('setPassword')
                else :
                    messages.success(request, f'Your answer is wrong')
            else :
                messages.success(request, f'Your answer is wrong')
    else:
        form = UserChangePasswordForm()
    return render(request, 'user/forgotPassword.html', {'form': form,'title':'Change password'})

def setPassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST) or None
        if form.is_valid():
            form.save()
            messages.success(request, f'Your password has been changed! You are now able to log in')
            return redirect('login')
        else:
            messages.success(request, f'Your password has not been changed!')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'user/setPassword.html', {'form': form,'title':'Create a new password'})
