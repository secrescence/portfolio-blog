from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import BlogPostForm


def blog_home(request):
    category = request.GET.get("category")  # This checks if the user clicked a category
    if category:
        posts = BlogPost.objects.filter(category=category).order_by("-created_at")
    else:
        posts = BlogPost.objects.all().order_by("-created_at")

    categories = (
        BlogPost.CATEGORY_CHOICES
    )  # This will send the categories to the template
    return render(request, "blog/home.html", {"posts": posts, "categories": categories})


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, "blog/detail.html", {"post": post})


def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_home")
    else:
        form = BlogPostForm()
    return render(request, "blog/create_post.html", {"form": form})
