# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from .models import Profile
from .forms import ProfileForm

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
    
            person = Profile.objects.create(user=user, address = request.POST['address'], nickname = request.POST['nickname']) #프로필 생성
            person.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')


def profile_update(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
        return redirect('people', request.user.username)
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'profile_update.html', {'profile_form':profile_form})


def people(request, username):
    #get_user_model() => User 클래스를 호출함
    people = get_object_or_404(get_user_model(), username = username)
    return render(request, 'people.html', {'people':people})
