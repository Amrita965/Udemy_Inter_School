from django.shortcuts import render
from django.views.generic import CreateView, ListView, ListView, DeleteView, UpdateView
from .forms import CourseForm
from .models import Course
from django.urls import reverse_lazy

# Create your views here.

class AddCourse(CreateView):
    template_name = 'Courses/course_form.html'
    form_class = CourseForm
    success_url = reverse_lazy('Courses:all_courses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Course'
        return context

class AllCourses(ListView):
    model = Course
    template_name = 'Courses/all_courses.html'
    context_object_name = 'courses'

class DeleteCourse(DeleteView):
    model = Course
    template_name ='Courses/course_delete.html'
    success_url = reverse_lazy('Courses:all_courses')
    pk_url_kwarg="pk"
    context_object_name = 'course'

class UpdateCourse(UpdateView):
    model = Course
    form_class = CourseForm
    template_name ='Courses/course_form.html'
    success_url = reverse_lazy('Courses:all_courses')
    pk_url_kwarg="pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Course'
        return context
