from django.shortcuts import render
from django.contrib import messages
from .forms import StudentForm
from .models import Student
from django.http import HttpResponseRedirect

def index(request):
	return render(request, 'student/index.html',{})


def add(request):
	form = StudentForm()
	if request.method=='POST':
		form = StudentForm(request.POST or None)
		if form.is_valid():
			print("3")
			form.save()
			messages.success(request,('Student Added Successfully!'))
			return render(request, 'student/add.html', {})
		else:
			return render(request, 'student/add.html', {'form':form})

	else:
		return render(request, 'student/add.html', {'form':form})
