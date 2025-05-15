from django.db import models

from django.db import models

class Car(models.Model):
    VIN = models.CharField(max_length=30, primary_key=True)
    model = models.CharField(max_length=30)
    productionYear = models.DateField()

class Client(models.Model):
    bankAccount = models.CharField(max_length=20, primary_key=True)
    FName = models.CharField(max_length=20)
    LName = models.CharField(max_length=20)

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    orderDate = models.DateField()
    totalPrice = models.IntegerField()

class SparePart(models.Model):
    sparePartID = models.AutoField(primary_key=True)
    partName = models.CharField(max_length=30)
    partPrice = models.IntegerField()
    partQuantity = models.IntegerField()

class Service(models.Model):
    serviceID = models.AutoField(primary_key=True)
    serviceName = models.CharField(max_length=30)
    servicePrice = models.IntegerField()

class Employee(models.Model):
    employeeID = models.AutoField(primary_key=True)
    FName = models.CharField(max_length=30)
    LName = models.CharField(max_length=30)
    empPosition = models.CharField(max_length=20)

