from django.urls import path
from . import views

urlpatterns=[  
    path('', views.index, name = 'home'),
    path('list', views.view_list, name= 'list'),
    path('delete_task/<str:pk>', views.delete_task, name = 'delete_task'),
    path('edit_edit/<str:pk>', views.edit_task, name = 'edit_task'),
    path('sort', views.sort, name = 'sort'),
    path('mark_done/<str:pk>', views.mark_done, name = 'mark_done') 

]


