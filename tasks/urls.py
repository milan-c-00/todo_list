from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.all_tasks, name='all_tasks'),
    path('create', views.create_task, name='create_task'),
    path('<int:task_id>/done', views.done_task, name='done_task'),
    # path('<int:task_id>/edit', views.edit_task, name='edit_task'),
    path('<int:task_id>/delete', views.delete_task, name='delete_task')
]
