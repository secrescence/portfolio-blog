from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("post/<int:post_id>/", views.blog_detail, name="blog_detail"),
]
