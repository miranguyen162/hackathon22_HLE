from django.contrib.auth import views as auth_views
from django.urls import path
from class_app import views

urlpatterns = [
    path('frontpage/', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('', views.home, name = 'home')
]
