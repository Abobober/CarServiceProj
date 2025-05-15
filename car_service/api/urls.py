from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='car_list'),
    path('cars/<str:vin>/', views.car_detail, name='car_detail'),
    path('cars/create/', views.car_create, name='car_create'),
    path('cars/<str:vin>/edit/', views.car_update, name='car_update'),
    path('cars/<str:vin>/delete/', views.car_delete, name='car_delete'),
]
