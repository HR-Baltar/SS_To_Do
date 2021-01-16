from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "list"),
    path('delete/<str:pk>/', views.deleteTask, name = "delete"),
    path('quickSort', views.quickSort, name= "quickSort")
]