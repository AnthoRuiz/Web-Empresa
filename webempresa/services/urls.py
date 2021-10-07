from django.urls import path
from . import views

urlpatterns = [
    # path Services
    path('', views.services, name="services"),
]
