from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect


from .models import post, category
from .forms import CommentFrom


# Create your views here.
def home(request):
    posts = post.objects.filter(status=post.ACTIVE).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)


def detail(request, id):
    post = get_object_or_404(post, id=id, status=post.ACTIVE)


    if request.method == 'POST':
        form = CommentFrom(request.POST)


        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()


            return redirect('post_detail')
        else:
            form = CommentFrom()


    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/detail.html', context)
