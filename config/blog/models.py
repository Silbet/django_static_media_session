from django.db import models
import os
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', null=True)

    def __str__(self):
        return self.title
    
@receiver(post_delete, sender=Blog)
def delete_blog_image(sender, instance, **kwargs):
    if instance.image and instance.image.path and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)