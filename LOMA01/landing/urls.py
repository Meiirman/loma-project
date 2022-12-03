from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.landing_page, name='home'),
    path('index/', views.index, name='index'),
# landing_page.html

]
