from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import PostForm, CommentForm

def post_list(request):
    list_template = 'myboard/post_list.html',
    posts = Post.objects.order_by('-created_at')
    return render(request, list_template, {"post_list": posts})


def post_add(request):
    add_template = 'myboard/post_add.html'
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.save()
            return redirect('detail_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, add_template, {'form': form})


def post_edit(request, pk):
    edit_template = 'myboard/post_add.html'
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, edit_template, {'form': form})


def post_detail(request, pk):
    detail_template = 'myboard/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    return render(request, detail_template, {'post': post})

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.commented_at = timezone.now()
            comment.save()
            return redirect('detail_post', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'myboard/add_comment_to_post.html', {'form': form})

def edit_comment(request, pk, c_pk):
    edit_template = 'myboard/add_comment_to_post.html'
    comment = get_object_or_404(Comment, pk=c_pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail_post', pk=pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, edit_template, {'form': form})

