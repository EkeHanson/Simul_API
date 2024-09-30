from rest_framework import serializers
from .models import UserMessage, Reply

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)  # Include replies in the message serializer
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)
    user_last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = UserMessage
        fields = '__all__'  # Include all fields, plus first_name and last_name

    def to_representation(self, instance):
        # Get the original representation
        representation = super().to_representation(instance)

        # Check if the request method is GET
        if self.context['request'].method == 'GET':
            # Add the user's first name and last name to the representation
            representation['user_first_name'] = instance.user.first_name
            representation['user_last_name'] = instance.user.last_name
            representation['user_email'] = instance.user.email
        else:
            # Optionally remove the first_name and last_name for other methods
            representation.pop('user_first_name', None)
            representation.pop('user_last_name', None)
            representation.pop('user_email', None)

        return representation
