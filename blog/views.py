# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, render


from .models import post, category


# Create your views here.
def home(request):
    posts = post.objects.filter(status=post.ACTIVE).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)
