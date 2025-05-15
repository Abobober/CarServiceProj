from django.db import models

class Car(models.Model):
    VIN = models.CharField(max_length=30, primary_key=True, db_column='VIN')
    model = models.CharField(max_length=30, blank=True, null=True, db_column='model')
    productionYear = models.DateField(blank=True, null=True, db_column='productionYear')

    class Meta:
        managed = False
        db_table = 'Car'


class Client(models.Model):
    bankAccount = models.CharField(max_length=20, primary_key=True, db_column='bankAccount')
    FName = models.CharField(max_length=20, blank=True, null=True, db_column='FName')
    LName = models.CharField(max_length=20, blank=True, null=True, db_column='LName')

    class Meta:
        managed = False
        db_table = 'Client'


class Order(models.Model):
    orderID = models.AutoField(primary_key=True, db_column='orderID')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, db_column='client')
    orderDate = models.DateField(blank=True, null=True, db_column='orderDate')
    totalPrice = models.IntegerField(blank=True, null=True, db_column='totalPrice')

    class Meta:
        managed = False
        db_table = 'Order'


class SparePart(models.Model):
    sparePartID = models.AutoField(primary_key=True, db_column='sparePartID')
    partName = models.CharField(max_length=30, blank=True, null=True, db_column='partName')
    partPrice = models.IntegerField(blank=True, null=True, db_column='partPrice')
    partQuantity = models.IntegerField(blank=True, null=True, db_column='partQuantity')

    class Meta:
        managed = False
        db_table = 'SparePart'


class Service(models.Model):
    serviceID = models.AutoField(primary_key=True, db_column='serviceID')
    serviceName = models.CharField(max_length=30, blank=True, null=True, db_column='serviceName')
    servicePrice = models.IntegerField(blank=True, null=True, db_column='servicePrice')

    class Meta:
        managed = False
        db_table = 'Service'


class Employee(models.Model):
    employeeID = models.AutoField(primary_key=True, db_column='employeeID')
    FName = models.CharField(max_length=30, blank=True, null=True, db_column='FName')
    LName = models.CharField(max_length=30, blank=True, null=True, db_column='LName')
    empPosition = models.CharField(max_length=20, blank=True, null=True, db_column='empPosition')

    class Meta:
        managed = False
        db_table = 'Employee'
