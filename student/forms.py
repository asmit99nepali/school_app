from django.core import validators
from django import forms
from .models import Student
from django.core.exceptions import ValidationError

class StudentForm(forms.ModelForm):
	name = forms.CharField(required=True , widget=forms.TextInput(attrs={"placeholder": "Enter Your Name.", "class":"form-control"}))
	roll = forms.IntegerField(required=True , widget=forms.TextInput(attrs={"placeholder": "Enter Your Roll.", "class":"form-control"}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter Your Email", "class": "form-control"}))
	address = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter Your Address", "class": "form-control"}))
	phone = forms.IntegerField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter Your Phone", "class": "form-control"}))
	parents = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter Your Parents", "class": "form-control"}))
	photo = forms.ImageField(required=True, widget=forms.FileInput(attrs={"class": "form-control"}))
	class Meta:
		model = Student
		fields = ["name", "roll", "email", "address", "phone", "parents","photo"]

	# def clean(self):
	# 	super(StudentForm, self).clean()

	# 	name = self.cleaned_data.get('name')
	# 	print(name)
	# 	if name is None:
	# 		print("name field is required")
	# 		raise forms.ValidationError("Name filed is required")
	# 		self._errors['name'] = self.error_class(['Name field is required'])

	# 	elif len(name) < 5:
	# 		print("Less than 5 characters")
	# 		raise forms.ValidationError("Miminum 5 characters required.")
	# 		self._errors['name'] = self.error_class(['Miminum 5 characters required'])

	# 	return self.cleaned_data

	def clean_name(self, *agrs, **kwargs):
		name = self.cleaned_data["name"]
		if (name.isspace()):	
			print("This filed is required")	
			raise forms.ValidationError("Name filed is required")
			# self._errors['name'] = self.error_class(['Name field is required'])

		elif len(name) < 5:
			print("Less than 5 characters")
			raise forms.ValidationError("Miminum 5 characters required.")
			# self._errors['name'] = self.error_class(['Miminum 5 characters required'])

		return name
	
	def clean_roll(self, *args, **kwargs):
		roll  = self.cleaned_data["roll"]
		if roll is None:
			raise forms.ValidationError("Roll No. field is required")
		return roll

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data["email"]
		if email is None :
			raise forms.ValidationError("Email field is required")
		return email
	
	def clean_phone(self, *args, **kwargs):
		phone = self.cleaned_data["phone"]
		if phone is None:
			raise forms.ValidationError("Phone field is required")
		return phone
