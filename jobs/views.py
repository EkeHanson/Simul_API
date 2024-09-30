from rest_framework import viewsets
from .models import Jobs
from .serializers import JobsSerializer
from rest_framework.permissions import AllowAny


class JobsView(viewsets.ModelViewSet):
    permission_classes = [AllowAny] 
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
