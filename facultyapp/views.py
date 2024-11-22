from django.contrib import auth
from django.contrib.auth import authenticate
from django.core.checks import messages
from django.shortcuts import render,redirect

from .forms import ADDCourseForm, MarksForm
# from ..adminapp.models import StudentList


def FacultyHomePage(request):
    return render(request,'facultyapp/FacultyHomePage.html')

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

# from .forms import ADDCourseForm

def add_course(request):
    if request.method == 'POST':
        form = ADDCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FacultyHomePage')
    else:
        form = AddCourse()

    return render(request, 'facultyapp/add_course.html', {'form': form})


# from .models import AddCourse
# import adminapp.models import StudentList
#
# def view_student_list(request):
#     course = request.GET.get('course')
#     section = request.GET.get('section')
#     student_courses = AddCourse.objects.all()
#     if course:
#         student_courses = student_courses.filter(course=course)
#     if section:
#         student_courses = student_courses.filter(section=section)
#     students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
#     course_choices = AddCourse.COURSE_CHOICES
#     section_choices = AddCourse.SECTION_CHOICES
#     context = {
#         'students': students,
#         'course_choices': course_choices,
#         'section_choices': section_choices,
#         'selected_course': course,
#         'selected_section': section,
#     }
#     return render(request, 'facultyapp/view_student_list.html', context)

from .models import AddCourse
from adminapp.models import *  # Corrected import

def view_student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()

    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)

    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))

    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES

    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }

    return render(request, 'facultyapp/view_student_list.html', context)

from django.core.mail import send_mail
from django.contrib.auth.models import User  # Assuming User is your custom user model
def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()

            # Retrieve the User email based on the student in the form
            student = marks_instance.student
            student_user = student.user
            user_email = student_user.email

            subject = 'Marks Entered'
            message = f'Hello, {student_user.first_name}  marks for {marks_instance.course} have been entered. Marks: {marks_instance.marks}'
            from_email = '2300033583@kluniversity.in'
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'facultyapp/marks_success.html')
    else:
        form = MarksForm()
    return render(request, 'facultyapp/post_marks.html', {'form': form})


