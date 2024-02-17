from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.controllers.service import ServiceView, ServiceDetailView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('services/', ServiceView.as_view(), name='create_list_service'),
    path('services/<int:id>/', ServiceDetailView.as_view(), name='detail_service'),
]

