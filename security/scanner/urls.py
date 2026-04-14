# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('scan/', views.scan_document, name='scan'),
    path('', views.welcome, name='welcome'),
    path("login/",views.login_view,name='login')
    # path('logout/', views.custom_logout, name='logout'),  # assuming this exists
]