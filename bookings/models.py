from django.db import models
from users.models import CustomUser  

class Booking(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookins')  # Link to the user who sent the message
    meeting_date = models.DateTimeField()
    subject = models.CharField(max_length=255)
    details = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.client.username} on {self.meeting_date}"
