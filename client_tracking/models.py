# client_tracking/models.py
from django.db import models

class ClientIP(models.Model):
    ip_address = models.GenericIPAddressField()
    session_id = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class GDPRConsent(models.Model):
    client_ip = models.ForeignKey(ClientIP, on_delete=models.CASCADE)
    consent_given = models.BooleanField(default=False)
    consent_timestamp = models.DateTimeField(auto_now_add=True)
