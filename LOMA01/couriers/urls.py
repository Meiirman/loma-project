from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.couriers),
    path('request/', views.courier_requests),
    path('new/', views.new_courier),
    path('<int:courier_id>/info/', views.courier_info),
    path('<int:courier_id>/delete_courier/', views.delete_courier),
    path('<int:courier_id>/courier_update/', views.courier_update),
    
]


# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('', views.orders,name='new_order'),
#     path('<int:order_id>/info/', views.order_info),

# ]