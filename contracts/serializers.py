from rest_framework import serializers

from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ["date_created", "date_updated", "id"]
