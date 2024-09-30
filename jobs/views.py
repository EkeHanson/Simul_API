from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Jobs
from .serializers import JobsSerializer
from rest_framework.permissions import AllowAny

class JobsView(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    permission_classes = [AllowAny]

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
