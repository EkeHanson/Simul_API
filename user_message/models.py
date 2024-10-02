from django.db import models

from django.db import models
from users.models import CustomUser  # Adjust the import based on your project structure

class UserMessage(models.Model):
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='messages')  # Link to the user who sent the message
    full_name = models.CharField(max_length=225, null=True, blank=True)  # Example: 09037494084
    userEmail = models.EmailField(max_length=80, null=True, blank=True)  # Allow nulls temporarily
    phone_number = models.CharField(max_length=15)  # Example: 09037494084
    address = models.CharField(max_length=255)  # Example: Road 19 Rumukurishi New Layout Porthacourt
    postal_code = models.CharField(max_length=10)  # Example: 44509
    service_of_interest = models.CharField(max_length=100)  # Field for service of interest
    description = models.TextField()  # Description field
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the message was created
    updated_at = models.DateTimeField(auto_now=True)  # Track when the message was last updated

    def __str__(self):
        return f"{self.service_of_interest} - {self.phone_number}"


class Reply(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='replies')
    full_name = models.CharField(max_length=225, null=True, blank=True)  # Example: 09037494084
    message = models.ForeignKey(UserMessage, related_name='replies', on_delete=models.CASCADE)
    userEmail = models.EmailField(max_length=80, null=True, blank=True)  # Allow nulls temporarily
    parent = models.ForeignKey('self', null=True, blank=True, related_name='sub_replies', on_delete=models.CASCADE)
    reply_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    admin_user = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Reply to {self.message.service_of_interest} - {self.created_at}"
