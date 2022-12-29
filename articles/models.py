from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

# article

class article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("articles")   

# comment tb 
class Comment(models.Model): # new
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse("articles")