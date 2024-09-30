from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'client', 'meeting_date', 'subject', 'details', 'is_confirmed', 'created_at']
        read_only_fields = ['id', 'is_confirmed', 'created_at']
