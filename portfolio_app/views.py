from django.shortcuts import render


# Create your views here.
def portfolio_home(request):
    return render(request, "portfolio_app/home.html")


def projects(request):
    return render(request, "portfolio_app/projects.html")


def about(request):
    return render(request, "portfolio_app/about.html")


def blog_home(request):
    return render(request, "blog/blog_home.html")
