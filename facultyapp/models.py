from django.db import models
from adminapp.models import StudentList


class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD', 'PYTHON FULL STACK DEVELOPMENT'),
    ]

    SECTION_CHOICES = [
        ('S11', 'SECTION S11'),
        ('S12', 'SECTION S12'),
        ('S13', 'SECTION S13'),
        ('S14', 'SECTION S14'),
        ('S15', 'SECTION S15'),
    ]

    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def __str__(self):
        return f'{self.student.Register_Number} - {self.course}  ({self.section})'

class Marks(models.Model):
    COURSE_CHOICES=[
        ('AOOP', 'ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD' , 'PYTHON FULL STACK DEVELOPMENT'),
    ]
    student = models.ForeignKey(StudentList, on_delete =models.CASCADE)
    course=models.CharField(max_length=50,choices=COURSE_CHOICES)
    marks =models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.course}"
