from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.CharField(max_length=160)
    keywords = models.CharField(max_length=255)
    content = models.TextField()
    post_img = models.ImageField(upload_to='post_img/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title