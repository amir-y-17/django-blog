from django.db import models
from blog.models import Post
from users.models import User


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        indexes = [models.Index(fields=["-date"])]

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"
