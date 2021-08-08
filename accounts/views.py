# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required


def signup_view(request):
    # 로그인한 유저는 접근 금지
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # user 저장
            user = form.save()
            # profile 생성
            person = Profile.objects.create(user=user, address=request.POST['address'], nickname=request.POST['nickname'])
            person.save()
            # 자동 login
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})


def login_view(request):
    # 로그인한 유저는 접근 금지
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                # 원래 가려고 했던 페이지로 이동하거나 home으로 이동
                return redirect(request.GET.get('next') or 'home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
        return redirect('profile', request.user.username)
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'profile_form':profile_form})


def profile(request, username):
    #get_user_model() => User 클래스를 호출함
    user_info = get_object_or_404(get_user_model(), username = username)
    posts_list = user_info.profile.post_participated.all
    return render(request, 'profile.html', {'user_info':user_info, 'posts_list': posts_list})
