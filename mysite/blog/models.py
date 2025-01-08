from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = "PB", 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    class Meta:
        # -publish (why - inorder to sort the newest to the oldest)
        ordering = ['-publish']
        #inorder to get query quickly and reqular 
        indexes = [
            models.Index(fields=['-publish']),
        ]


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        #we got "blog:post_detail" from path('<int:id>/', views.post_detail, name='post_detail'),
        return reverse("blog:post_detail", args=[self.id])
    

    ########################end***** post class***** ##########################
    
class Anmar(models.Model):
    name = models.CharField(max_length=100)