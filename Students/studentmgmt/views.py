
from django.shortcuts import render, redirect, get_object_or_404

import Students
from studentmgmt.models import Student


# Create your views here.
def students_list(request):
    students = Student.objects.all()
    return render(request, 'studentmgmt/students_list.html', {'students': students})

def students_create(request):
    if request.method == "POST":
        roll_number = request.POST['roll_number']
        name = request.POST['name']
        age = request.POST['age']
        Student.objects.create(roll_number=roll_number, name=name, age=age)
        return redirect('students_list')
    return render(request, 'studentmgmt/student_form.html')


def student_update(request, roll_number):
    student = get_object_or_404(Student, roll_number=roll_number)
    if request.method == "POST":
        student.roll_number = request.POST['roll_number']
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.save()
        return redirect('students_list')
    return render(request, 'studentmgmt/student_update.html', {'student': student})

def students_delete(request, roll_number):
    student = get_object_or_404(Student, pk=roll_number)
    if request.method == "POST":
        student.delete()
        return redirect('students_list')
    return render(request, 'studentmgmt/student_delete.html')

