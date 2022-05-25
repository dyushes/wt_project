from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('registr/', views.registr),
    path('login', views.login),
    path('jobvacancy', views.jobvacancy)
]
