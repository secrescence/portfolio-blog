from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import BlogPostForm
from django.core.paginator import Paginator
import markdown
from django.utils.safestring import mark_safe


def blog_home(request):
    category = request.GET.get("category")  # This checks if the user clicked a category
    if category:
        posts = BlogPost.objects.filter(category=category).order_by("-created_at")
    else:
        posts = BlogPost.objects.all().order_by("-created_at")

    # Pagination
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = (
        BlogPost.CATEGORY_CHOICES
    )  # This will send the categories to the template
    return render(
        request, "blog/home.html", {"page_obj": page_obj, "categories": categories}
    )


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    post.content_html = mark_safe(markdown.markdown(post.content))
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


def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog_detail", post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, "blog/edit_post.html", {"form": form, "post": post})


def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("blog_home")
    return render(request, "blog/delete_post_confirm.html", {"post": post})
