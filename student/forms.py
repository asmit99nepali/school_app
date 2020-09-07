from django.core import validators
from django import forms
from .models import Student
from django.core.exceptions import ValidationError

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ["name", "roll", "email", "address", "phone", "parents"]

	def clean(self):
		super(StudentForm, self).clean()

		name = self.cleaned_data.get('name')
		print(name)
		if name is None:
			print("name field is required")
			raise forms.ValidationError("Name filed is required")
			self._errors['name'] = self.error_class(['Name field is required'])

		elif len(name) < 5:
			print("Less than 5 characters")
			raise forms.ValidationError("Miminum 5 characters required")
			self._errors['name'] = self.error_class(['Miminum 5 characters required'])

		return self.cleaned_data