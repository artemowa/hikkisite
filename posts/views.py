from django.shortcuts import render

from .models import Post


def post_lists(request):
	posts = Post.objects.all()
	return render(request, 'posts/index.html', context={'posts': posts})