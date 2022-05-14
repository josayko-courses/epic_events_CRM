from rest_framework import serializers

from crm.models import Client


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
