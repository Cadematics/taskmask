from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name = 'todolist_page'),
    path('new_task/', views.new_task, name = 'new_task_page'),
    path('delete/<int:task_id>', views.delete_task, name = 'delete_task_page'),
    path('edit/<int:task_id>', views.edit_task, name = 'edit_task_page'),
    path('completed/<int:task_id>', views.completed_task, name = 'completed_task_page'),
    path('pending/<int:task_id>', views.pending_task, name = 'pending_task_page'),
]
