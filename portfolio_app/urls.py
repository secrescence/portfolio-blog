from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path("", views.portfolio_home, name="portfolio_home"),
    path("projects/", views.projects, name="projects"),
    path("about/", views.about, name="about"),
    path("blog.html", views.blog_home, name="blog_home"),
]
