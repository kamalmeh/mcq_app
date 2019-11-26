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
from django.urls import path

from mcq import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('admin_view/', views.admin_view, name="admin"),
    path('create_test', views.create_test_view, name='test creation'),
    path('edit_test', views.edit_test_view, name='edit test'),
    path('test', views.test_view, name='test'),
    path('', views.home_view, name='home'),
]
