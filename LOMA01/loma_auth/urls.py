from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.login),
    # path('reg/', views.registration),
    path('', views.registration, name='reg'),
    path('submite/', views.registrate_user),

]