from django.urls import path

from . import views

urlpatterns=[
    path('',views.login, name='login'),
    path('register',views.register, name='register'),
    path('adminlog',views.admin,name='admin'),
    path('display',views.display,name="display"),
    path('logout', views.logout, name='logout'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('view_user',views.view_user,name='view_user'),
    path('add_user',views.add_user,name='add_user'),
    path('edit_user',views.edituser,name='edituser'),
    path('deleteuser',views.deleteuser,name='deleteuser'),
    path('view_category',views.viewcategory,name='viewcategory'),
    path('addcategory',views.addcategory,name="addcategory")
]