from django.contrib import admin
from django.urls import path,include
from MyApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),

    # Client APIs
    path('GET/clients/', views.ClientsView.as_view(), name='client-list-create'),
    path('GET/clients/<cid>/', views.ClientOp.as_view(), name='client-detail'),

    # Project APIs
    path('GET/projects/', views.ProjectsView.as_view(), name='project-list-create'),
    path('GET/projects/<pid>/', views.ProjectOp.as_view(), name='project-detail'),

    # Projects assigned to logged-in user
    path('user/projects/', views.User_Assigned_ProjectsView.as_view(), name='user-projects'),
    
]
