from rest_framework import viewsets
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from .models import News
from rest_framework import status
from .serializers import NewsSerializer
from rest_framework.permissions import AllowAny


class NewsView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    # def create(self, request, *args, **kwargs):
    #     print("POST request data:", request.data)  # Print the request data to the terminal
    #     response = super().create(request, *args, **kwargs)
        
    #     if response.status_code != status.HTTP_201_CREATED:  # Check if the response is not a 201 Created
    #         print("Serializer errors:", response.data)  # Print the serializer errors to the terminal

    #     return response

    # def partial_update(self, request, *args, **kwargs):
    #     print("PATCH request data:", request.data)  # Print the request data to the terminal
    #     response = super().partial_update(request, *args, **kwargs)

    #     if response.status_code != status.HTTP_200_OK:  # Check if the response is not a 200 OK
    #         print("Serializer errors:", response.data)  # Print the serializer errors to the terminal

    #     return response

