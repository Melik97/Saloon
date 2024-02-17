from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

# from authorize.models import User
from ..models import Service


class ServiceSerializer(ModelSerializer):
    # created_by_pk = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     source='created_by',
    #     write_only=True,
    # )

    class Meta:
        model = Service
        fields = ['id', 'title', 'description']
