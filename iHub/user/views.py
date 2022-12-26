from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserChangePasswordForm, ChangePasswordForm, UserForm
from .models import followUser, users, shares, postComment, images
from django.contrib.auth.models import User   ##save details about user such as sequrity question
from django.contrib.auth.hashers import make_password ##save password encrypted
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, CommentForm


def index(request):
    return render(request, 'user/index.html',{'title':'index'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES) or None
        if form.is_valid():
            email1 = request.POST.get('email')
            email2= request.POST.get('verify_email')
            if email1 != email2:
                messages.info(request, f'Mail adresses are not matched, please check!')
            else:
                form.save()      
                en=users(username=request.POST.get('username'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),security_question=request.POST.get('security_question'),answer=request.POST.get('answer'),image="", occupation="", interest="", bio="", followers=0,followings=0)
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
            return redirect('home')
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
                        messages.info(request, f'Answer is wrong')
                else:
                    messages.info(request, f'Security question is wrong')
            else:
                messages.info(request, f'Account does not exit please sign in')
    else:
        form = UserChangePasswordForm()
    return render(request, 'user/forgotPassword.html', {'form': form,'title':'Change password'})

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
    return render(request, 'user/setPassword.html', {'form': form,'title':'Change password'})

def userPage(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        username = request.user
        db_shares=shares(username=username,subject=request.POST.get('subject'),label=request.POST.get('label'),private=request.POST.get('private'),type=request.POST.get('type'),value=request.POST.get('value'),comment=request.POST.get('comment'))
        db_shares.save()
        messages.success(request,('Your profile was successfully updated!'))
        return redirect ("userPage")
    shares_list = shares.objects.all()
    user_form = UserForm(request.POST)
    user_list = users.objects.get(username=request.user)
    image = users.objects.get(username=request.user).image
    return render(request = request, template_name ="user/userPage.html", context = {"user":request.user, "user_form": user_form, "shares_list":shares_list, 'image':image, 'user_list':user_list})

def homePage(request):
    users_list = users.objects.all()
    followers_list = followUser.objects.all()
    subject_list = shares.objects.order_by().values('subject').distinct()
    shares_list= []
    for f in subject_list:
        shares_list += shares.objects.filter(id=shares.objects.filter(subject = f.get("subject")).last().id)
    return render(request, template_name ="user/home.html", context = {"user":request.user, "shares_list":shares_list, "users_list":users_list,"followers_list":followers_list })

def follow(request, follower_name):
    username = request.user
    follower = follower_name
    db_follow=followUser(username=username,followers=follower)
    db_follow.save()
    user = users.objects.get(username=request.user.username)
    user.followings = 1 + user.followings
    user.save()
    shares_list = shares.objects.all()
    users_list = users.objects.all()
    followers_list = followUser.objects.all()
    return render(request, template_name ="user/home.html", context = {"user":request.user, "shares_list":shares_list, "users_list":users_list,"followers_list":followers_list })

def unfollow(request, follower_name):
    username = request.user
    follower = follower_name
    delete_record = followUser.objects.get(username=username,followers=follower)
    followUser.objects.filter(id=delete_record.id).delete()
    user = users.objects.get(username=request.user.username)
    user.followings = user.followings - 1
    user.save()
    shares_list = shares.objects.all();
    users_list = users.objects.all();
    followers_list = followUser.objects.all();
    return render(request, template_name ="user/home.html", context = {"user":request.user, "shares_list":shares_list, "users_list":users_list,"followers_list":followers_list })

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            occupation=request.POST.get('occupation')
            interest=request.POST.get('interest')
            bio=request.POST.get('bio')
            image = user_form.cleaned_data.get("image") 
            obj = images.objects.create(username=request.user.username, img = img ) 
            obj.save()
            user = users.objects.filter(username=request.user.username)
            user.update(first_name=first_name,last_name=last_name,occ=occupation,interest=interest,bio=bio,image=image)
            user = User.objects.filter(username=request.user.username)
            user.update(first_name=first_name,last_name=last_name)
            return redirect ("userPage")
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'user/profile.html', {'user_form': user_form})

def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = User.objects.filter(username__icontains=query)
        follower_list = followUser.objects.filter(username=request.user)
    return render(request, 'user/search.html', {'query': query, 'results': results, 'follower_list':follower_list})

def searchShare(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search_share')
        if query == '':
            query = 'None'
        results = shares.objects.filter(comment__icontains=query)
    return render(request, 'user/search_share.html', {'query': query, 'results': results})

def postDetail(request, post_id):
    post = shares.objects.get(id=post_id)
    if postComment.objects.all is None:
        comment_list=None
    else:
        comment_list=postComment.objects.filter(post_id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=request.POST.get('comment')
            post_comment=postComment(post_id=post_id, username = request.user.username, comment=comment)
            post_comment.save();
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'user/post_detail.html', { 'form':form, 'share': post, 'comment_list':comment_list})

def subjectDetail(request, subject):
    subject_list = shares.objects.filter(subject__icontains=subject)
    return render(request, 'user/subject_detail.html', { 'subject_list':subject_list})

def followingDetail(request, user):
    results = []
    if request.method == "GET":
        results = followUser.objects.filter(username=user)
    return render(request, 'user/following_list.html', {'results': results})

def followerDetail(request, user):
    results = []
    if request.method == "GET":
        results = followUser.objects.filter(followers=user)
    return render(request, 'user/follower_list.html', {'results': results})

def post(request):
    if request.method == "POST":
        print("post")
        user_form = UserForm(request.POST)
        username = request.user
        db_shares=shares(username=username,subject=request.POST.get('subject'),label=request.POST.get('label'),private=request.POST.get('private'),type=1,content=request.POST.get('content'),description=request.POST.get('description'))
        db_shares.save()
        return redirect ("home")
    else:
        user_form = UserForm(request.POST)
    return render(request, template_name ="user/post.html", context = {"user":request.user, "user_form": user_form})