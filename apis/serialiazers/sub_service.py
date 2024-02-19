from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

# from authorize.models import User
from ..models import SubService


class SubServiceSerializer(ModelSerializer):
    # created_by_pk = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     source='created_by',
    #     write_only=True,
    # )

    class Meta:
        model = SubService
        fields = ['id', 'name', 'description', 'price', 'duration_minutes', 'service']
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=SubService.objects.all(), message=("Name already exists"))]
            },
        }