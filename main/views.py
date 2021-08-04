# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Image
from .forms import PostForm, PostSearchForm
from django.db.models import Q
from django.views.generic import FormView

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts_list': posts})

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            # for images
            for img in request.FILES.getlist('imgs'):
                image = Image()
                image.post = post
                image.image = img
                image.save()  
            
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'new.html',{'form':form})

def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'detail.html', {'post':post})

def edit(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        # 이후에 프론트에서의 수정방식에 따라 form = post로 변경
        form = PostForm(instance=post)
    return render(request, 'edit.html',{'form':form})

def delete(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return redirect('home')



class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(body__icontains=searchWord) | Q(deadline__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)