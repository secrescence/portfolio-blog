from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),  # home page
    path("post/<int:post_id>/", views.blog_detail, name="blog_detail"),  # blog detail
    path("create/", views.create_post, name="create_post"),  # create post
    path("post/<int:post_id>/edit/", views.edit_post, name="edit_post"),  # edit post
    path(
        "post/<int:post_id>/delete/", views.delete_post, name="delete_post"
    ),  # delete post
]
