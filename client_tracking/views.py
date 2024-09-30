from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ClientIP, GDPRConsent
from .serializers import ClientIPSerializer, GDPRConsentSerializer

class ClientIPViewSet(viewsets.ModelViewSet):
    queryset = ClientIP.objects.all()
    serializer_class = ClientIPSerializer
    permission_classes = [AllowAny]  # Allow IP tracking for any visitor

class GDPRConsentViewSet(viewsets.ModelViewSet):
    queryset = GDPRConsent.objects.all()
    serializer_class = GDPRConsentSerializer
    permission_classes = [AllowAny]  # GDPR consent is open to any visitor

    def perform_create(self, serializer):
        client_ip = ClientIP.objects.get(ip_address=self.request.data.get('ip_address'))
        serializer.save(client_ip=client_ip)
