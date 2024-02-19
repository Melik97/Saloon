from django.db import transaction
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ..models import Service
from ..serialiazers import ServiceSerializer


class ServiceView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = []
        else:
            self.permission_classes = []
            # self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super(ServiceView, self).get_permissions()

    @transaction.atomic
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Service.objects.all()


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = 'id'

    def get_object(self):
        service = Service.objects.filter(id=self.kwargs[self.lookup_field])
        obj = get_object_or_404(service)

        return obj

