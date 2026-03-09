from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('create-ticket/', views.create_ticket, name='create_ticket'),

]