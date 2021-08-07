from django.shortcuts import render
from main.models import Post
from main.forms import PostSearchForm
from django.views.generic import FormView
from django.db.models import Q

# Create your views here.
#오프라인 온라인 배달 카테고리 페이지 나눈것

def offline_category(request):
    posts = Post.objects.all().filter(category='오프라인')
    return render(request, 'offline.html', {'posts':posts})

def online_category(request):
    posts = Post.objects.all().filter(category='온라인')
    return render(request, 'online.html', {'posts':posts})

def delivery_category(request):
    posts = Post.objects.all().filter(category='배달음식')
    return render(request, 'delivery.html', {'posts':posts})

#오프라인용 리서치

class SearchFormView_of(FormView):
    form_class = PostSearchForm
    template_name = 'offline.html'

    def form_valid(self, form):
        posts = Post.objects.all().filter(category='오프라인')
        searchWord = form.cleaned_data['search_word']
        post_list = posts.filter(Q(title__icontains=searchWord) | Q(body__icontains=searchWord) | Q(deadline__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

#온라인용 리서치

class SearchFormView_on(FormView):
    form_class = PostSearchForm
    template_name = 'online.html'

    def form_valid(self, form):
        posts = Post.objects.all().filter(category='온라인')
        searchWord = form.cleaned_data['search_word']
        post_list = posts.filter(Q(title__icontains=searchWord) | Q(body__icontains=searchWord) | Q(deadline__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)


#배달음식용 리서치

class SearchFormView_de(FormView):
    form_class = PostSearchForm
    template_name = 'delivery.html'

    def form_valid(self, form):
        posts = Post.objects.all().filter(category='배달음식')
        searchWord = form.cleaned_data['search_word']
        post_list = posts.filter(Q(title__icontains=searchWord) | Q(body__icontains=searchWord) | Q(deadline__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)