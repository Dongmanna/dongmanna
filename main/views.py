# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm, PostSearchForm
from django.db.models import Q
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from chat.views import sendNotice


def home(request, category):
    # 카테고리별 게시글
    if category == 'All':
        posts_list = Post.objects.all()
    else:
        posts_list = Post.objects.all().filter(category=category)
    # 참가중인 채팅방
    posts_participated = request.user.profile.post_participated.all()
    # 마감임박 게시글
    posts = Post.objects.all()
    for post in posts:
        if post.members.count() != post.limit - 1 or posts_participated.filter(pk=post.pk):
            posts=posts.exclude(pk=post.pk)
    posts_orderby_deadline = posts.order_by('deadline')
    return render(request, 'home.html', {'posts_list': posts_list, 'posts_participated': posts_participated, 'posts_orderby_deadline': posts_orderby_deadline, 'category': category})


# CRUD

@login_required
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.published_date = timezone.now()
            post.region = request.user.profile.address
            post.save()

            # 게시글을 작성하면 자동으로 공구에 참여
            post.members.add(post.author)
            post.author.post_participated.add(post)

            # 게시글을 생성하고 곧바로 채팅방 생성을 위해 newRoom 함수로 이동
            return redirect('chat:newRoom', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'new.html', {'form': form})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post': post})


def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 작성자만 수정할 수 있도록 함
    if request.user != post.author.user:
        return redirect('detail', pk=post.pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.published_date = timezone.now
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        # 이후에 프론트에서의 수정방식에 따라 form = post로 변경
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 작성자만 삭제할 수 있도록 함
    if request.user != post.author.user:
        return redirect('detail', pk=post.pk)

    post.delete()
    return redirect('home', 'All')


# Search

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'home.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']

        # 카테고리별로 보기
        if (category := self.request.POST.get('category')) != 'All':
            posts = Post.objects.all().filter(category=category)
            post_list = posts.filter(Q(title__icontains=searchWord) | Q(
                body__icontains=searchWord) | Q(deadline__icontains=searchWord)).distinct()
        # 전체보기
        else:
            post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(
                body__icontains=searchWord) | Q(deadline__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['posts_list'] = post_list
        context['category'] = category

        return render(self.request, self.template_name, context)


# 공구 참여

@login_required
def post_participated_toggle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile = request.user.profile

    # 글쓴이는 공구 참여/취소 버튼을 누를 필요가 없으므로 detail 페이지로 redirect
    if profile == post.author:
        return redirect('detail', pk)

    check_participated_post = profile.post_participated.filter(pk=pk)

    # 공구에 이미 참여중인 경우 공구 취소 버튼이 작동
    if check_participated_post.exists():
        sendNotice(profile.nickname + "님이 채팅방을 나갔습니다. (%d/%d)"%(post.members.count()-1, post.limit), pk)
        post.members.remove(profile)
        profile.post_participated.remove(post)
        post.save()
    # 공구에 아직 참여하지 않았고 모집인원이 남아있는 경우 공구 참여 버튼이 작동
    elif post.members.count() < post.limit:
        sendNotice(profile.nickname + "님이 채팅방에 입장했습니다. (%d/%d)"%(post.members.count()+1, post.limit), pk)
        post.members.add(profile)
        profile.post_participated.add(post)
        post.save()
    return redirect('detail', pk)
