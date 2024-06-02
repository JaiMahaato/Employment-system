"""
URL configuration for emp_mana_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.jai,name='jai'),
    path('home/', views.emp,name='emp'),
    path('home/add/',views.add,name='add'),
    path('delete/<int:emp_id>', views.delete,name='delete'),
    path('update/<int:emp_id>',views.update,name='update'),
    path('doupdate/<int:emp_id>',views.doupdate,name='doupdate'),
    path('feedback/',views.feedback,name='feedback'),
     path('testimonials/',views.testimonials,name='testimonials'),
    
]
