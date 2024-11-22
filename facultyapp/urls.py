from django.urls import path, include
from . import views
urlpatterns = [
    path('FacultyHomePage/', views.FacultyHomePage, name='FacultyHomePage'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    path('add_course/', views.add_course, name='add_course'),
    path('view_student_list/', views.view_student_list, name='view_student_list'),
    path('post_marks/', views.post_marks, name='post_marks'),

]