from django.urls import path

from . import views

app_name= 'item'

urlpatterns = [
    path('<int:pk>/' , views.detail , name='detail'),
    #path('project/<int:pk>/', views.project_detail, name='project'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('project/<int:pk>/', views.edit_project, name='edit_project'),
]