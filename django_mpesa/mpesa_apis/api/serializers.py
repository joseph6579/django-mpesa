from rest_framework import serializers
from mpesa_apis.models import LNMTransaction


class LNMSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = LNMTransaction

