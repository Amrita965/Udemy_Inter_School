from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import StudentForm
from .models import Student
from django.urls import reverse_lazy

# Create your views here.

class AddStudent(CreateView):

    form_class = StudentForm
    template_name ='Students/student_form.html'
    success_url = reverse_lazy('Students:all_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Student'
        return context

class AllStudents(ListView):
    model = Student
    template_name = 'Students/all_students.html'
    context_object_name ='students'

class DeleteStudent(DeleteView):
    model = Student
    template_name ='Students/student_delete.html'
    success_url = reverse_lazy('Students:all_students')
    pk_url_kwarg="pk"
    context_object_name = 'student'

class UpdateStudent(UpdateView):
    model = Student
    form_class = StudentForm
    template_name ='Students/student_form.html'
    success_url = reverse_lazy('Students:all_students')
    pk_url_kwarg="pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Student'
        return context

    

