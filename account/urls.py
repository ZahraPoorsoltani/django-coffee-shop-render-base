"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from account.views import *
from django.contrib.auth import views as auth_views
from django.urls import reverse,include

app_name = 'account'
urlpatterns = [
    path('login/',login_view,name='login_view'),

    path('logout/',logout_view,name='logout_view'),
    path('signup/',signup_view,name='signup_view'),
    
    
    # 1) enter email address to send email 
    path('password_reset/', auth_views.PasswordResetView
        .as_view(template_name="password-reset.html",
                email_template_name = 'password_reset_confirm.html',
                success_url = 'done/'), 
        name='password_reset'),
    #2) show successfull message to sent email
     path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name="password_reset_done",
    ),
    
    # 3) email link clicked 
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name=
                                                    'password_reset_new.html',
                                                    success_url= '/account/reset/done/'),
        name="password_reset_confirm"
    ),
    # 4) password changed message
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'),
        name="password_reset_complete",
    ),
    path('test',test_view)
     


    

    
]
urlpatterns += [
    path('captcha/', include('captcha.urls')),
]