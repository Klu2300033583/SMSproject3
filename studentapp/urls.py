from django.urls import path, include
from . import views

urlpatterns = [
    path('studenthomepage/', views.StudentHomePage, name='StudentHomePage'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    path('view_marks/', views.view_marks, name='view_marks'),
]