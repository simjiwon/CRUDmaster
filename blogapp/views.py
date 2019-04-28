from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    posts = Blog.objects
    return render(request, 'home.html', {"posts": posts})

def detail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {"post": post})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['head']
    blog.body = request.POST['info']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, blog_id):
    destroy = get_object_or_404(Blog, pk=blog_id)
    destroy.delete()
    return redirect('home')

def update(request, blog_id):
    text = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {"text": text})

def edit(request, blog_id):
    edit = Blog.objects.get(pk=blog_id)
    edit.title = request.POST['head']
    edit.body = request.POST['info']
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('home')