# Generated by Django 5.0.14 on 2025-05-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('VIN', models.CharField(db_column='VIN', max_length=30, primary_key=True, serialize=False)),
                ('model', models.CharField(blank=True, db_column='model', max_length=30, null=True)),
                ('productionYear', models.DateField(blank=True, db_column='productionYear', null=True)),
            ],
            options={
                'db_table': 'Car',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('bankAccount', models.CharField(db_column='bankAccount', max_length=20, primary_key=True, serialize=False)),
                ('FName', models.CharField(blank=True, db_column='FName', max_length=20, null=True)),
                ('LName', models.CharField(blank=True, db_column='LName', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeID', models.AutoField(db_column='employeeID', primary_key=True, serialize=False)),
                ('FName', models.CharField(blank=True, db_column='FName', max_length=30, null=True)),
                ('LName', models.CharField(blank=True, db_column='LName', max_length=30, null=True)),
                ('empPosition', models.CharField(blank=True, db_column='empPosition', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.AutoField(db_column='orderID', primary_key=True, serialize=False)),
                ('orderDate', models.DateField(blank=True, db_column='orderDate', null=True)),
                ('totalPrice', models.IntegerField(blank=True, db_column='totalPrice', null=True)),
            ],
            options={
                'db_table': 'Order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('serviceID', models.AutoField(db_column='serviceID', primary_key=True, serialize=False)),
                ('serviceName', models.CharField(blank=True, db_column='serviceName', max_length=30, null=True)),
                ('servicePrice', models.IntegerField(blank=True, db_column='servicePrice', null=True)),
            ],
            options={
                'db_table': 'Service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('sparePartID', models.AutoField(db_column='sparePartID', primary_key=True, serialize=False)),
                ('partName', models.CharField(blank=True, db_column='partName', max_length=30, null=True)),
                ('partPrice', models.IntegerField(blank=True, db_column='partPrice', null=True)),
                ('partQuantity', models.IntegerField(blank=True, db_column='partQuantity', null=True)),
            ],
            options={
                'db_table': 'SparePart',
                'managed': False,
            },
        ),
    ]
