import io
# import form
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib import messages  # Correct import for messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *

def projecthomepage(request):
    return render(request, 'adminapp/ProjectHomePage.html')

def printpagecall(request):
    return render(request, 'adminapp/printer.html')

def printpagelogic(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        print(f"User Input: {user_input}")
        context = {'user_input': user_input}
        return render(request, 'adminapp/printer.html', context)
    return redirect('printpagecall')

def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        context = {'result': result, 'error': error_message}
        return render(request, 'adminapp/ExceptionExample.html', context)
    return redirect('exceptionpagecall')

def UserRegisterPageCall(request):
    return render(request, 'adminapp/UserRegisterPage.html')

# def UserRegisterLogic(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         first_name = request.POST.get('first_name', '')
#         last_name = request.POST.get('last_name', '')
#         email = request.POST.get('email', '')
#         pass1 = request.POST.get('password', '')
#         pass2 = request.POST.get('password1', '')
#
#         if pass1 == pass2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'OOPS! Username already taken.')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'OOPS! Email already registered.')
#             else:
#                 user = User.objects.create_user(
#                     username=username,
#                     password=pass1,
#                     first_name=first_name,
#                     last_name=last_name,
#                     email=email
#                 )
#                 user.save()
#                 messages.success(request, 'Account created successfully!')
#                 return redirect('projecthomepage')
#
#         else:
#             messages.error(request, 'Passwords do not match.')
#         return redirect('UserRegisterPageCall')
#     return render(request, 'adminapp/UserRegisterPage.html')

import re
def UserRegisterLogic(request):
   if request.method == 'POST':
        username = request.POST.get('username', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        pass1 = request.POST.get('password', '')
        pass2 = request.POST.get('password1', '')

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
            else:
                # Check if email contains four consecutive digits
                if re.search(r'\d{4}', email):
                    # Register as faculty
                    user = User.objects.create_user(
                        username=username,
                        password=pass1,
                        first_name=first_name,
                        last_name=last_name,
                        email=email
                    )
                    # Here you can assign the faculty-specific roles or groups
                    # For example:
                    # user.groups.add(Group.objects.get(name='Faculty'))
                    user.save()
                    messages.success(request, 'Faculty account created successfully!')
                else:
                    # Register as student
                    user = User.objects.create_user(
                        username=username,
                        password=pass1,
                        first_name=first_name,
                        last_name=last_name,
                        email=email
                    )
                    # Here you can assign the student-specific roles or groups
                    # For example:
                    # user.groups.add(Group.objects.get(name='Student'))
                    user.save()
                    messages.success(request, 'Student account created successfully!')

                return redirect('projecthomepage')
        else:
            messages.error(request, 'Passwords do not match.')
        return redirect('UserRegisterPageCall')
   return render(request, 'adminapp/UserRegisterPage.html')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    context = {'form': form, 'tasks': tasks}
    return render(request, 'adminapp/add_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')
# def loginCall(request):
#     return render(request, 'adminapp/loginpage.html')

def loginlogic(request):
    return render(request, 'adminapp/loginpage.html')

from django.contrib.auth import get_user_model
def loginpagecall(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return render(request, 'studentapp/StudentHomepage.html')# Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return render(request, 'facultyapp/FacultyHomepage.html')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/loginpage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/loginpage.html')
    else:
        return render(request, 'adminapp/loginpage.html')


# def loginpagecall(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         User = get_user_model()
#         try:
#             user = User.objects.get(email=email)
#             user = authenticate(request, username=user.username, password=password)
#         except User.DoesNotExist:
#             user = None
#
#         if user is not None:
#             login(request, user)
#             # Check if the email contains the number "4" to route to the faculty page
#         else:
#             messages.error(request, 'Invalid email or password.')
#             return render(request, 'adminapp/loginpage.html')
#
#     return render(request, 'adminapp/loginpage.html')

def StudentHomePage(request):
    return render(request,'studentapp/StudentHomePage.html')

def FacultyHomePage(request):
    return render(request,'facultyapp/FacultyHomePage.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

# def add_student(request):
#     if request.method=='POST':
#         form=StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form =StudentForm()
#     return render(request, 'adminapp/add_student.html', {'form': form})


from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})
def student_list(request):
    students=StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})


from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid() and 'file' in request.FILES:
            file = request.FILES['file']
            file_extension = file.name.split('.')[-1].lower()  # Get the file extension

            try:
                # Use pd.read_csv() for CSV and pd.read_excel() for Excel files
                if file_extension == 'csv':
                    df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
                elif file_extension in ['xls', 'xlsx']:
                    df = pd.read_excel(file, parse_dates=['Date'], dayfirst=True)
                else:
                    return render(request, 'adminapp/Chart.html', {'form': form, 'error': 'Unsupported file format. Please upload a CSV or Excel file.'})
            except Exception as e:
                return render(request, 'adminapp/Chart.html', {'form': form, 'error': f"Error reading file: {str(e)}"})

            # Process sales data
            total_sales = df['Sales'].sum()
            average_sales = df['Sales'].mean()

            # Group by month and plot pie chart
            df['Month'] = df['Date'].dt.month
            monthly_sales = df.groupby('Month')['Sales'].sum()
            month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x - 1])

            plt.figure(figsize=(6, 6))
            plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%')
            plt.title('Sales Distribution per Month')

            # Save pie chart as base64-encoded image
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
            buffer.close()
            plt.close()

            return render(request, 'adminapp/Chart.html', {
                'form': form,
                'total_sales': total_sales,
                'average_sales': average_sales,
                'chart': image_data
            })
    else:
        form = UploadFileForm()
    return render(request, 'adminapp/Chart.html', {'form': form})

def datetimepagecall(request):
    return render(request, 'adminapp/datetimepage.html')

import datetime
import calendar
from datetime import timedelta

def datetimepagelogic(request):
    if request.method=="POST":
        number1=int(request.POST['date1'])
        x=datetime.datetime.now()
        ran =x+timedelta(days=number1)
        ran1=ran.year
        ran2=calendar.isleap(ran1)
        if ran2 ==False:
            ran3= "Not leap year"
        else:
            ran3="Leap year"
    a1={'ran': ran, 'ran3': ran3, 'ran1': ran1, 'number1': number1}
    return render(request, 'adminapp/datetimepage.html',a1 )
import random
import string

def randompagecall(request):
    return render(request, 'adminapp/randomexample.html')

def randomlogic(request):
    if request.method=="POST":
        number1=int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1={'ran':ran}
    return render(request,'adminapp/randomexample.html',a1)


def calculatorpagecall(request):
    return render(request, 'adminapp/calculator.html')
from django.shortcuts import render

def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else 'Infinity'
        except ValueError:
            result = 'Invalid input'

    return render(request, 'adminapp/calculator.html', {'result': result})



from django.shortcuts import render
from django.http import HttpResponse
from .models import Feedback

def feedbackpagecall(request):
    return render(request, 'adminapp/feedback_form.html')



def feedbacklogic(request):
    if request.method == 'POST':
        username = request.POST.get('feedname')
        email = request.POST.get('feedemail')
        feedback_text = request.POST.get('feedback')

        print(username, email, feedback_text)  # Debug: print to console

        # Save to database
        Feedback.objects.create(username=username, email=email, feedback=feedback_text)
        return redirect('feedbackpagecall')

    return render(request, 'adminapp/feedback_form.html')

