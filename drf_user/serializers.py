from rest_framework import serializers
from user.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'work_position', 'is_active', 'is_blocked')
        read_only_fields = ('id',)
