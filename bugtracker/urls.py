from django.contrib import admin
from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, ProjectView, PostTableView, ProjectCreateView, ProjectListView
from . import views

urlpatterns = [
    path('', views.Tracker, name='bugtracker'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),   
    path('projects/<int:pk>/', ProjectView.as_view(), name='project-detail'),   
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    path('projects/<int:pk>/tables', PostTableView.as_view(), name="tables-view"),
    path('tables/', views.Tables, name='tables'),
    path('list/', PostListView.as_view(), name='post-list'),
    #path('projects/', views.Projects, name='projects'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'), 

]
