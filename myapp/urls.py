from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.jai,name='jai'),
    path('register/', views.register_view,name='register_view'),
    path('login/', views.login_view,name='login_view'),
    path('logout/', views.logout_view,name='logout_view'),
    path('dashboard/', views.dashboard_view,name='dashboard_view'),
   
]  