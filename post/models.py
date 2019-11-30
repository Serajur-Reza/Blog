from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    category=models.ManyToManyField('Category')
    body=models.TextField()
    comment_count=models.IntegerField(default=0)
    view_count=models.IntegerField(default=0)
    thumbnail=models.ImageField()
    author=models.ForeignKey('Author', on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    publish=models.DateTimeField(default=timezone.now)
    view=models.IntegerField(default=0)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={
            'pk': self.pk
        })

    @property
    def get_comments(self):
        return self.comments.all()

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    class Meta:
        ordering=('-publish',)

    

class PostView(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    comment=models.TextField()
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

    class Meta:
        ordering=('-time',)

class Author(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture=models.ImageField()

    def __str__(self):
        return self.user.username