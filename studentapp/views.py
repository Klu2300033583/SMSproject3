from django.contrib import auth
from django.contrib.auth import authenticate
from django.core.checks import messages
from django.shortcuts import redirect, render


def StudentHomePage(request):
    return render(request,'studentapp/StudentHomePage.html')


def UserLoginPageCall(request):
     return render(request, 'adminapp/UserLoginPage.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/UserLoginPage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/UserLoginPage.html')
    else:
        return render(request, 'adminapp/UserLoginPage.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

from django.contrib.auth.models import User
from adminapp.models import StudentList
from facultyapp.models import Marks
from django.shortcuts import render

def view_marks(request):
    user = request.user
    try:
        student_user=User.objects.get(username=user.username)
        student = StudentList.objects.get(Register_Number=student_user)
        marks=Marks.objects.filter(student=student)
        return render(request,'studentapp/view_marks.html', {'marks': marks})
    except (StudentList.DoesNotExist, User.DoesNotExist):
        return render(request,'studentapp/no_studentlist.html',{'error': 'No student record found for this user.'})