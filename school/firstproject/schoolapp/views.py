from django.shortcuts import render
from schoolapp.forms import NewSchoolForm
from schoolapp import models
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def newStudent(request):
    form=NewSchoolForm()
    res=render(request,'new_student.html',{'form':form})
    return res

def add(request):
    if request.method == 'POST':
        form=NewSchoolForm(request.POST)
        school=models.School()
        school.name=form.data['name']
        school.roll=form.data['roll']
        school.standard=form.data['standard']
        school.father=form.data['father']
        school.save()
    s="Record Stored<br><a href='view-students'>View All Students </a>"
    return HttpResponse(s)


def viewStudent(request):
    students=models.School.objects.all()
    res=render(request,'view_student.html',{'students':students})
    return res

def deleteStudent(request):
    studentid=request.GET['studentid']
    school=models.School.objects.filter(id=studentid)
    school.delete()
    return HttpResponseRedirect('view-students')

def editStudent(request):
    student=models.School.objects.get(id=request.GET['studentid'])
    fields={'name':student.name,'roll':student.roll,'standard':student.standard,'father':student.father}
    form=NewSchoolForm(initial=fields)
    res=render(request,'edit_book.html',{'form':form,'student':student})
    return res

def edit(request):
    if request.method=="POST":
        form=NewSchoolForm(request.POST)
        school=models.School()
        school.id=request.POST['studentid']
        school.name=form.data['name']
        school.roll=form.data['roll']
        school.standard=form.data['standard']
        school.father=form.data['father']
        school.save()
        return HttpResponseRedirect('view-students')
