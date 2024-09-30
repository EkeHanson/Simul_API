from rest_framework import serializers
from .models import ClientIP, GDPRConsent

class ClientIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientIP
        fields = ['id', 'ip_address', 'session_id', 'location', 'created_at']

class GDPRConsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GDPRConsent
        fields = ['id', 'client_ip', 'consent_given', 'consent_timestamp']
        read_only_fields = ['consent_timestamp']
