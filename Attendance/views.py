from django.shortcuts import render
from Students.models import Student
from Courses.models import Course
from django.utils.dateparse import parse_date
from .models import Attendance
from django.http import HttpResponse
# Create your views here.

def mark_attendance(request):
    courses = Course.objects.all()

    dict = {
        'courses': courses,
    }

    if request.method == 'POST':
        print(request.POST)
        date = request.POST.get('date')
        print(date)
        course_id = request.POST.get('course-id')
        course = Course.objects.get(id=course_id)
        students = Student.objects.filter(courses=course)

        dict['students'] = students
        dict['date'] = date
        dict['course'] = course
       

    return render(request, 'Attendance/mark_attendance.html', context=dict)
    