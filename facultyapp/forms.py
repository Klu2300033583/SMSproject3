from django import forms
from .models import *

class ADDCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']

from .models import Marks
class MarksForm(forms.ModelForm):
    class Meta:  # Corrected 'meta' to 'Meta'
        model = Marks
        fields = ['student', 'course', 'marks']
