from django.urls import path
from .views import AddStudent, AllStudents, DeleteStudent, UpdateStudent

app_name="Students"

urlpatterns = [
    path("students/", AllStudents.as_view(), name="all_students"),
    path("students/add/", AddStudent.as_view(), name="add_student"),
    path("students/<int:pk>/delete/", DeleteStudent.as_view(), name="delete_student"), 
    path('students/<int:pk>/edit/', UpdateStudent.as_view(), name='edit_student'),
]
