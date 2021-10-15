from django.urls import path

from . import views

urlpatterns=[
    path('',views.login, name='login'),
    path('register',views.register, name='register'),
    path('adminlog',views.admin,name='admin'),
    path('display',views.display,name="display"),
    path('logout', views.logout, name='logout')
]