"""taskapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),

   # Auth
   path('signup/', views.signupuser, name='signupuser'),
   path('logout/', views.logoutuser, name='logoutuser'),
   path('login/', views.loginuser, name='loginuser'),

  #tasks
   path('', views.home, name='home'),
   path('create/', views.createtask, name='createtask'),
   path('current/', views.currenttask, name='currenttask'),
   path('completed/', views.completedtasks, name='completedtasks'),
   path('task/<int:task_pk>', views.tasktodo, name='tasktodo'),
   path('task/<int:task_pk>/>complete', views.completedtask, name='completedtask'),
   path('task/<int:task_pk>/>delete', views.deletetask, name='deletetask'),


]
