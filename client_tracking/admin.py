# client_tracking/admin.py
from django.contrib import admin
from .models import ClientIP, GDPRConsent

admin.site.register(ClientIP)
admin.site.register(GDPRConsent)
