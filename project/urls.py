from django.urls import path

from . import views

urlpatterns = [
    path('', views.table, name='table'),
    path('table_two/', views.table_two, name='table_two')
]