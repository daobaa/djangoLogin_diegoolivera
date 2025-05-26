from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user-form/', views.user_form, name='user_form'),
    path('logout/', views.logout, name='logout'),
]