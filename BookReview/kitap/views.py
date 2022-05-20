import email
from django.shortcuts import redirect, render, get_object_or_404
from .forms import CustomRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from .forms import *
from django.contrib.auth.models import User

# Create your views here.
def authentication(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    register = CustomRegisterForm()
    if request.method == 'POST':    
        if request.POST.get('login-username') is None:
            register = CustomRegisterForm(request.POST)
            if register.is_valid():
                username = register.cleaned_data.get('username')
                email = register.cleaned_data.get('email')                
                subject = 'welcome to Kitap world'
                message = f'Hi { username }, thank you for registering in Kitap.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [ email ]
                send_mail( subject, message, email_from, recipient_list )
                
                register.save()
                
        else:
            username = request.POST.get('login-username')
            password = request.POST.get('login-password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')

    context = {'register': register}
    return render(request, 'kitap/authentication.html', context)

def logoutUser(request):
    logout(request)
    return redirect('authentication')

@login_required(login_url='authentication')
def index(request):
    return render(request, 'kitap/index.html')

@login_required(login_url='authentication')
def about(request):
    return render(request, 'kitap/about.html')

@login_required(login_url='authentication')
def categories(request):
    return render(request, 'kitap/categories.html')


@login_required(login_url='authentication')
def edit_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'kitap/edit_profile.html', context)

@login_required(login_url='authentication')
def profile(request, pk):
    user = User.objects.get(id=pk)
    email = user.email
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=load_profile(request.user))
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=load_profile(request.user))
 
    context = {
        'form': form,
        'email': email,
        }
    return render(request, 'kitap/profile.html', context)

@login_required(login_url='authentication')
def faq(request):
    return render(request, 'kitap/faq.html')

def load_profile(user):
    try:
        return user.profile
    except Exception:
        return Profile.objects.create(user=user)