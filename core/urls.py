from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.settings),
    path('couriers/', views.couriers),
    path('orders/', views.orders),
    path('products/', views.products),
    path('roles/', views.roles),
    path('<int:chat_id>/activate_courier/', views.activate_courier),

]