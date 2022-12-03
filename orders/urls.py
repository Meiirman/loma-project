from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.orders,name='orders'),
    path('new/', views.new_order),
    path('<int:order_id>/delete_order/', views.delete_order),
    path('<int:order_id>/info/', views.order_info),
    path('<int:order_id>/order_update/', views.order_update),

    
    path('products/', views.products),
    path('products/new/', views.new_product),
    path('products/<int:product_id>/delete_product/', views.delete_product),
    path('products/<int:product_id>/info/', views.product_info),
    path('products/<int:product_id>/product_update/', views.product_update),

]