from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

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
        fields = ['id', 'name', 'description']
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=Service.objects.all(), message=("Name already exists"))]
            },
        }

