from django.db.models import Count,Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, View

from .models import Post, PostView,Category, Comment,Author
from .forms import CommentForm
# Create your views here.


def category_count():
    category=Post.objects.values('category__title').annotate(Count('category__title'))
    return category

def show_post(request):
    category=category_count()
    most_recent=Post.objects.order_by('-publish')[0:3]
    print(most_recent)
    qs=Post.objects.all()
    paginator=Paginator(qs,2)
    page_request_var='page'
    page=request.GET.get(page_request_var)

    paginated_qs=paginator.get_page(page)
    context={
        'queryset':paginated_qs,
        'most_recent':most_recent,
        'page_request_var':page_request_var,
        'category_count':category_count
    }
    return render(request, 'blog.html', context)



def post(request, pk):
    post=get_object_or_404(Post, pk=pk)
    most_recent=Post.objects.order_by('-publish')[:3]
    category=category_count()
    
    PostView.objects.get_or_create(post=post)
    
    form=CommentForm(request.POST or None)

    if request.method=="POST":
        if form.is_valid():
            form.instance.user=request.user
            form.instance.post=post
            form.save()
            return redirect(reverse('post_detail', kwargs={
                'pk':post.pk
            }))

    context={
        'post':post,
        'most_recent':most_recent,
        'category_count':category_count,
        'form':form
    }
    return render(request, 'post.html', context)

def search(request):
    queryset=Post.objects.all()
    query=request.GET.get('s')

    if query:
        queryset=queryset.filter(Q(title__icontains=query)).distinct()

    context={
        'queryset':queryset
    }
    return render(request,'search_results.html', context)