from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.tasks, name='home'),
]
