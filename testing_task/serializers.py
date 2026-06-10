from rest_framework import serializers
from django.utils import timezone


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
    username = serializers.CharField(max_length=50, allow_blank=False, min_length=3)
    email = serializers.EmailField()


class ToDoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField()
    due_date = serializers.DateTimeField()
    user = UserSerializer()
    
    def create(self, validated_data):
        return validated_data
    
    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("The date is supposed to be today or ahead")
        return value
    
