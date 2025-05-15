import django_filters
from .models import Car, Client, Order, SparePart, Service, Employee

class CarFilter(django_filters.FilterSet):
    model = django_filters.CharFilter(lookup_expr='icontains')
    productionYear = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Car
        fields = ['VIN', 'model', 'productionYear']

class ClientFilter(django_filters.FilterSet):
    FName = django_filters.CharFilter(lookup_expr='icontains')
    LName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ['bankAccount', 'FName', 'LName']

class OrderFilter(django_filters.FilterSet):
    client__bankAccount = django_filters.CharFilter(field_name='client__bankAccount', lookup_expr='icontains')
    client__FName = django_filters.CharFilter(field_name='client__FName', lookup_expr='icontains')
    client__LName = django_filters.CharFilter(field_name='client__LName', lookup_expr='icontains')
    orderDate = django_filters.DateFromToRangeFilter()
    totalPrice = django_filters.RangeFilter()

    class Meta:
        model = Order
        fields = ['orderID', 'client__bankAccount', 'client__FName', 'client__LName', 'orderDate', 'totalPrice']

class SparePartFilter(django_filters.FilterSet):
    partName = django_filters.CharFilter(lookup_expr='icontains')
    partPrice = django_filters.RangeFilter()
    partQuantity = django_filters.RangeFilter()

    class Meta:
        model = SparePart
        fields = ['partName', 'partPrice', 'partQuantity']

class ServiceFilter(django_filters.FilterSet):
    serviceName = django_filters.CharFilter(lookup_expr='icontains')
    servicePrice = django_filters.RangeFilter()

    class Meta:
        model = Service
        fields = ['serviceName', 'servicePrice']

class EmployeeFilter(django_filters.FilterSet):
    FName = django_filters.CharFilter(lookup_expr='icontains')
    LName = django_filters.CharFilter(lookup_expr='icontains')
    empPosition = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['FName', 'LName', 'empPosition']
