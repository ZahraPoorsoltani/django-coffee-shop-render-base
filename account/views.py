from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from account.utils import CustomBackend
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from account.forms import CustomAuthenticationForm,CustomUserCreationForm,CaptchaTestForm
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from website.utils import add_err
from django.contrib import messages


# Create your views here.
def test_view(request):
    form = CaptchaTestForm()
    return render(request,'test.html',{'form':form})
def login_view(request):
    
    form = CustomAuthenticationForm()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = CustomBackend.authenticate(request,username=username,password = password)
                if user is not None:
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,f'{username}, خوش آمدید:)')
                    return redirect('/')
                else:
                    messages.add_message(request,messages.ERROR,'نام کاربری یا رمز عبور اشتباه است!')

            
            else:
                add_err(request,form.errors)              

        return render(request,'login.html',{'form':form})
    return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')





def signup_view(request):
    form = CustomUserCreationForm()
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = CustomUserCreationForm(request.POST)
            
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,f'ثبت نام با موفقیت انجام شد.')
                return redirect(reverse('account:login_view'))
            
            add_err(request,form.errors)

            return render(request,'register.html',{'form':form})
        
        # print(form)
        return render(request,'register.html',{'form':form})
    return redirect('/')


def pass_reset_view(request):
    form =PasswordResetForm()
    return render(request,'password-reset.html',{'form':form})