from django.contrib import admin
from django.urls import path, include, re_path
from landing import views   
from core import views as core_views
from orders import views as products_views
urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^telegrambot/', include('telegrambot.urls', namespace="telegrambot")),


    path('reg/', include('loma_auth.urls')),
    path('orders/', include('orders.urls')),
    path('couriers/', include('couriers.urls')),
    path('tasks/', include('tasks.urls')),
    path('settings/', include('core.urls')),
    
    path('', include('landing.urls')),
    path('home/', include('landing.urls')),

    # re_path('/?', views.er404)

    path('auth/', include('django.contrib.auth.urls')),
    path('auth/login/orders/',products_views.orders_red),
    path('dashboard/',products_views.orders ),
    path('products/',products_views.products ),
]