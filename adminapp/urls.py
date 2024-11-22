# from django.urls import path, include
# from . import views
#
# urlpatterns = [
#     path('',views.projecthomepage, name = 'projecthomepage'),
#     path('printpagecall/',views.printpagecall, name='printpagecall'),
#     path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
#     path('exceptionpagecall/',views.exceptionpagecall, name='exceptionpagecall'),
#     path('exceptionpagelogic/',views.exceptionpagelogic, name='exceptionpagelogic'),
#     path('UserRegisterPageCall/',views.UserRegisterPageCall, name='UserRegisterPageCall'),
#     path('UserRegisterLogic/',views.UserRegisterLogic, name='UserRegisterLogic'),
#     path('add_task/', views.add_task, name='add_task'),
#     path('<int:pk>/delete/', views.delete_task, name='delete_task'),
#     path('loginpagecall/', views.loginpagecall, name='loginpagecall'),
#     # path('logout/', views.loginpagecall, name='logout'),
# ]
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),  # Home page route
    # Print page and exception page routes with original names
    path('printpagecall/', views.printpagecall, name='printpagecall'),
    path('printpagelogic/', views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),

    # User registration and login routes with original names
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('loginpagecall/', views.loginpagecall, name='loginpagecall'),
    path('loginlogic/', views.loginlogic, name='loginlogic'),

    path('logout/', views.logout, name='logout'),  # Uncomment this when the logout view is available
    path('studenthomepage/', views.StudentHomePage, name='StudentHomePage'),
    path('facultyhomepage/', views.FacultyHomePage, name='FacultyHomePage'),

    # Task-related routes with original names
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('calculatorpagecall/', views.calculatorpagecall, name='calculatorpagecall'),
    path('upload_file/', views.upload_file, name='upload_file'),
    # path('upload_filepagecall/', views.upload_filepagecall, name='upload_filepagecall'),

    path('feedbackpagecall/', views.feedbackpagecall, name='feedbackpagecall'),
    path('feedbacklogic/', views.feedbacklogic, name='feedbacklogic'),

]
