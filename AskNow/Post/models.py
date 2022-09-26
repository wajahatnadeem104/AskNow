from django.db import models
from User.models import User
from ckeditor.fields import RichTextField
from Post.utils import post_image_location


class Post(models.Model):
    title = models.CharField(max_length=30, null=False,
                             blank=False, unique=True)
    body = RichTextField(max_length=500, null=True, blank=True)
    image = models.ImageField(
        upload_to=post_image_location, null=True, blank=True)
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name='date published')
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name='date updated')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    upvotes = models.ManyToManyField(
        User, related_name='post_upvotes', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='post_downvotes', blank=True)

    def total_votes(self):
        return (self.upvotes.count() - self.downvotes.count())

    def __str__(self):
        return self.title + '-' + self.author.username


class Comment(models.Model):
    blog_post = models.ForeignKey(Post, related_name='comments',
                                  on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    body = models.TextField(max_length=225)
    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name='date added')

    def __str__(self):
        return self.blog_post.title + '-' + self.username + '-' + str(self.date_added.date())
