# Create your views here.
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'polls/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'polls/post_detail.html', {'post': post})
    