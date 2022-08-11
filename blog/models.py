from django.db import models
# Import to use the logged in user as the article author.
from django.contrib.auth.models import User


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=150, unique=True)
    # slug is a newspaper term. It is short label generally used in URLs
    # and contain only letters, numbers, underscores or hyphens.
    slug = models.SlugField()
    body = models.TextField()
    # Field authomatically populated when the user submits the article
    date = models.DateTimeField(auto_now_add=True)
    # Field to add a thumbnail for the blog article
    thumbnail = models.ImageField(default="default.png", blank=True)
    # Field to associate the articles with the user that created it. The user
    # in this case is the logged in User that the system registers.
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    """Method to return only a part of the body and display this snippet
    instead of the whole body of the article"""
    def snippet(self):
        return f"{self.body[:100]}..."
