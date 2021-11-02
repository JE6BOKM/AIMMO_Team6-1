from django.db import models

from apps.posts.models import Post
from apps.users.models import User


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, help_text="Post")
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE, help_text="User")
    parent = models.ForeignKey(
        "self", related_name="reply", on_delete=models.CASCADE, null=True, blank=True, help_text="Check_parent_comment"
    )
    comment = models.CharField(max_length=500, help_text="Comment")
    created_at = models.DateTimeField("created_time", auto_now_add=True, help_text="created time")
    updated_at = models.DateTimeField(auto_now=True, null=True, help_text="updated time")
