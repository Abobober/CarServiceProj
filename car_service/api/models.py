from django.db import models

class Car(models.Model):
    VIN = models.CharField(primary_key=True, max_length=30)
    model = models.CharField(max_length=30, blank=True, null=True)
    productionYear = models.DateField(blank=True, null=True)

    class Meta:
        managed = False  # Django не создаст таблицу, т.к. она уже есть
        db_table = 'Car'

class Client(models.Model):
    bankAccount = models.CharField(primary_key=True, max_length=20)
    FName = models.CharField(max_length=20, blank=True, null=True)
    LName = models.CharField(max_length=20, blank=True, null=True)
    cars = models.ManyToManyField(Car, through='ClientCars')

    class Meta:
        managed = False
        db_table = 'Client'

class ClientCars(models.Model):
    bankAccount = models.ForeignKey(Client, on_delete=models.DO_NOTHING, db_column='bankAccount')
    VIN = models.ForeignKey(Car, on_delete=models.DO_NOTHING, db_column='VIN')

    class Meta:
        managed = False
        db_table = 'ClientCars'
        unique_together = (('bankAccount', 'VIN'),)

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, db_column='client')
    orderDate = models.DateField(blank=True, null=True)
    totalPrice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Order'

class SparePart(models.Model):
    sparePartID = models.AutoField(primary_key=True)
    partName = models.CharField(max_length=30, blank=True, null=True)
    partPrice = models.IntegerField(blank=True, null=True)
    partQuantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SparePart'

class Service(models.Model):
    serviceID = models.AutoField(primary_key=True)
    serviceName = models.CharField(max_length=30, blank=True, null=True)
    servicePrice = models.IntegerField(blank=True, null=True)
    parts = models.ManyToManyField(SparePart, through='ServiceParts')

    class Meta:
        managed = False
        db_table = 'Service'

class ServiceParts(models.Model):
    serviceID = models.ForeignKey(Service, on_delete=models.DO_NOTHING, db_column='serviceID')
    sparePartID = models.ForeignKey(SparePart, on_delete=models.DO_NOTHING, db_column='sparePartID')

    class Meta:
        managed = False
        db_table = 'ServiceParts'
        unique_together = (('serviceID', 'sparePartID'),)

class Employee(models.Model):
    employeeID = models.AutoField(primary_key=True)
    FName = models.CharField(max_length=30, blank=True, null=True)
    LName = models.CharField(max_length=30, blank=True, null=True)
    empPosition = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Employee'