from django.db import models
from django.utils import timezone
from datetime import timedelta

def get_default_start_date():
    return timezone.now().date()

def get_default_end_date():
    return timezone.now().date() + timedelta(days=1)

class Jobs(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField(default=get_default_start_date)  # Use callable
    end_date = models.DateField(default=get_default_end_date)      # Use callable
    requirements = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title
