from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, ClientViewSet, OrderViewSet, SparePartViewSet, ServiceViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'spareparts', SparePartViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
