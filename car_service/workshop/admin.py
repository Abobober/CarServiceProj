from django.contrib import admin

from django.contrib import admin
from .models import Car, Client, Order, SparePart, Service, Employee

admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(SparePart)
admin.site.register(Service)
admin.site.register(Employee)