from rest_framework import serializers
from .models import Jobs
from django.utils import timezone
from datetime import timedelta

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"

