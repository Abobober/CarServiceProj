from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Car, Client, Order, SparePart, Service, Employee
from .serializers import (
    CarSerializer, ClientSerializer, OrderSerializer,
    SparePartSerializer, ServiceSerializer, EmployeeSerializer
)
from .filters import (
    CarFilter, ClientFilter, OrderFilter,
    SparePartFilter, ServiceFilter, EmployeeFilter
)

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('VIN')
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('bankAccount')
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientFilter

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('orderID')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

class SparePartViewSet(viewsets.ModelViewSet):
    queryset = SparePart.objects.all().order_by('sparePartID')
    serializer_class = SparePartSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SparePartFilter

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('serviceID')
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('employeeID')
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter
