from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import TeacherForm
from .models import Teacher
from django.urls import reverse_lazy

# Create your views here.

class AddTeacher(CreateView):
    template_name = 'Teachers/teacher_form.html'
    form_class = TeacherForm
    success_url = '/dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Teacher'
        return context
    
class AllTeachers(ListView):
    model = Teacher
    template_name = 'Teachers/all_teachers.html'
    context_object_name ='teachers'


class UpdateTeacher(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name ='Teachers/teacher_form.html'
    success_url = reverse_lazy("Teachers:all_teachers.html")
    pk_url_kwarg="pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Teacher'
        return context

class DeleteTeacher(DeleteView):
    model = Teacher
    template_name ='Teachers/teacher_delete.html'
    success_url = reverse_lazy("Teachers:all_teachers.html")
    pk_url_kwarg="pk"