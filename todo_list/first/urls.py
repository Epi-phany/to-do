from django.urls import path
from .views import (TaskList,
TaskDetail, 
TaskCreateView, 
TaskUpdate, 
TaskDelete,
Register,
Loggin)
from django.contrib.auth import views as auth_views

urlpatterns =[
  path('',TaskList.as_view(),name='home'),
  path('login/',Loggin.as_view(),name='login'),
   path('register/',Register.as_view(),name='register'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'first/logout.html'),name='logout'),
  path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
  path('create-task/',TaskCreateView.as_view(),name='create-task'),
  path('update-task/<int:pk>/',TaskUpdate.as_view(),name='update-task'),
  path('delete-task/<int:pk>/',TaskDelete.as_view(),name='delete-task'),
]                                                                                          