from dataclasses import fields

from rest_framework import serializers
from clients.models import Clients
from .services import make_sha256_hash


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class ClientRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data) -> Clients:
        validated_data['password'] = make_sha256_hash(validated_data['password'])
        return Clients.objects.create(**validated_data)

