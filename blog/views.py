from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


def home(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def sidebar(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request,'blog/no-sidebar.html', context)

def single_post(request):
    return render(request,'blog/single-post.html')

def error(request):
    return render(request,'blog/404.html')


class CreateVIEW(CreateView):
    model = Posts
    template_name = 'CRUD/create.html'
    fields = ('img', 'name', 'about', 'join_date', 'comment')


class UpdateVIEW(UpdateView):
    model = Posts
    template_name = 'CRUD/edit.html'
    fields = ('img', 'name', 'about', 'join_date', 'comment')


class DeleteVIEW(DeleteView):
    model = Posts
    template_name = 'CRUD/delete.html'
    success_url = reverse_lazy('blog-home')
