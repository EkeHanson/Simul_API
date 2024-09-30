from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
