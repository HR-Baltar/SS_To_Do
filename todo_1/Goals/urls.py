from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "list"),
    path('deleteWarning/<str:pk>', views.delete, name="delete"),
    path('update_task/<str:pk>', views.update_task, name="update_task"),
    path('mark_done/<str:pk>', views.mark_done, name='mark_done'),
    path('sort_tasks', views.sort_tasks, name = 'sort_tasks')
]