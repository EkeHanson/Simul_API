from rest_framework import viewsets
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from .models import News
from .serializers import NewsSerializer
from rest_framework.permissions import AllowAny


class NewsView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

