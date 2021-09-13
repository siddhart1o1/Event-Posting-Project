from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Post, Like
# Create your views here.
from .forms import EventForm
from django.http import HttpResponseRedirect


def Post_view(request):
    qs = Post.objects.all()
    user = request.user
    context = {
        "qs": qs,
        "user": user,
    }
    return render(request, "posts/index.html", context)


def add_post(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_post?submitted=True")
    else:
        form = EventForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "posts/form.html", {"form": form, "submitted": submitted})


def like_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.Liked.all():
            post_obj.Liked.remove(user)
        else:
            post_obj.Liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == "Like":
                like.value = "Unlike"
            else:
                like.value = "Like"
        like.save()
    return redirect("posts:post-list")
