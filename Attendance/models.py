from django.db import models
from Students.models import Student
from Courses.models import Course

# Create your models here.

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.student} - {self.course}'
