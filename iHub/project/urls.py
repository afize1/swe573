"""swe573 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# url management

from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth
 
urlpatterns = [
 
    path('admin/', admin.site.urls),
 
    path('', include('user.urls')),
    path('login/', user_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('register/', user_view.register, name ='register'),
    path('userPage', user_view.userPage, name ='userPage'),
    path('forgotPassword/', user_view.forgotPassword, name ='forgotPassword'),
    path('setPassword/<username>', user_view.setPassword, name ='setPassword'),
    path('home', user_view.homePage, name ='home'),
    path('follow/<follower_name>', user_view.follow, name ='follow'),
    path('search', user_view.search, name ='search'),
    path('search_share', user_view.searchShare, name ='search_share'),
]