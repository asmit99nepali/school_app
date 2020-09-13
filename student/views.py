from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import StudentForm
from .models import Student
from django.http import HttpResponseRedirect

def index(request):
	return render(request, 'student/index.html',{})


def add(request):
	form = StudentForm()
	if request.method=='POST':
		form = StudentForm(request.POST, request.FILES or None)
		if form.is_valid():
			# request.FILES['photo'].name, request.FILES['photo']
			form.save()
			messages.success(request,('Student Added Successfully!'))
			return render(request, 'student/add.html', {'form':form})
		else:
			return render(request, 'student/add.html', {'form':form})

	else:
		return render(request, 'student/add.html', {'form':form})

def show(request):
	students = Student.objects.all
	return render(request, 'student/show.html',{"students":students})

def edit(request, std_id):
	print(std_id)
	student = Student.objects.get(pk = std_id)

	if request.method == 'POST':
		form = StudentForm()
		form = student(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Student Updated Successfully!'))
			return render(request,'student/add.html', {'form':form})
		else:
			form = StudentForm(instance=student)
	return render(request, 'student/edit.html',{"from":form})

