from rest_framework import serializers
from contact.models import Cantact


class ContactCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cantact
        fields = "__all__"
