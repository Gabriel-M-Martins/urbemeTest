from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.tasks),
    path('tasks/add', views.addTask),
    path('tasks/update', views.update),
    path('tasks/<str:id>', views.onTask)
]