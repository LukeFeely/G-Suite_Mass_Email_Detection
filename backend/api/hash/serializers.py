from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Hashes

class HashesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashes
        fields = "__all__"