from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        help_text="작성자",
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, default="", help_text="카테고리"
    )
    title = models.CharField(max_length=255, help_text="제목")
    content = models.TextField(blank=True, help_text="내용")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
