from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.db.models.signals import post_delete
from Post.models import Post


@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(pre_save, sender=Post)
def pre_save_blog_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.author.username + '-' + instance.title)
