from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView


from django.shortcuts import render

from courses.models import Course


# Create your views here.
class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_delete.html'
    success_url = reverse_lazy('course_list')
