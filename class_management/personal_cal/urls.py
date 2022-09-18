from django.urls import path
from personal_cal import views

urlpatterns = [
    path('', views.home_cal, name = "home_cal"),
    path('email/', views.email, name = "email")
]

