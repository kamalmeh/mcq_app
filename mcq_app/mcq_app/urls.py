"""mcq_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path

from mcq import views

urlpatterns = [
    path('admin/', admin.site.urls, name='Django Admin'),
    path('admin_view/', views.admin_view, name="admin"),
    path('create_test', views.create_test_view, name='test creation'),
    path('edit_test', views.edit_test_view, name='edit test'),
    path('delete_test', views.delete_test_view, name='delete test'),
    path('all_tests', views.all_test_view, name='all test'),
    path('add_category', views.add_category, name='category'),
    path('add_question', views.add_question, name='question'),
    path('assign_test', views.assign_test_view, name='user_assign'),
    path('add_user', views.add_user_view, name='add_user'),
    path('edit_question', views.edit_question_view, name='Edit_Question'),
    path('test', views.test_view, name='test'),
    path('', views.home_view, name='home'),
    re_path(r'.*', views.display_error_view, name='error')
]
