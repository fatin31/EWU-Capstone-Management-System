
from django import forms

from .models import Student

# Create your forms here.

class StudentForm(forms.ModelForm):
	
	class Meta:
		model = Student
		fields = ['userName','fName','lName','email','password']

