from rest_framework import serializers
from .models import Spam

class SpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spam
        fields = ['id', 'phone_number', 'spam_count']
