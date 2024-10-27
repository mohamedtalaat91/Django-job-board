from django.contrib import admin
from django.urls import path , include
from . import views


app_name =  'job'
urlpatterns = [
    path('all', views.job_list, name='job_list'),
    path('<int:id>/', views.job_detail, name='job_detail'),
]