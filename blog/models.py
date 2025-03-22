from django.db import models


# Create your models here.


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ("Tech", "Tech"),
        ("Life", "Life"),
        ("Tutorial", "Tutorial"),
        ("News", "News"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Tech")

    def __str__(self):
        return self.title
