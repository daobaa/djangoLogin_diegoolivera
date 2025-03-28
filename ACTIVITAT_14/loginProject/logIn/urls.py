from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('access/', views.login, name='access'),
    path('user-form/', views.user_form, name='user_form')
]