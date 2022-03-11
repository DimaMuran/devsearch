from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects,name='projects'),
    path('search/', views.search, name='search'),
    path('project/<str:pk>/', views.project, name='project'),
    path('create-project/',views.createProject,name='create-project'),
    path('update-project/<str:pk>/',views.updateProject,name='update-project'),
    path('delete-project/<str:pk>/',views.deletePorject, name='delete-project'),

]