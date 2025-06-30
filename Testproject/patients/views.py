from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from patients.models import Patient


# Create your views here.
class PatientListView(ListView):
    model = Patient
    template_name = 'patient/patient_list.html'
    context_object_name = 'patients'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'
    context_object_name = 'patient'

class PatientCreateView(CreateView):
    model = Patient
    fields = '__all__'
    template_name = 'patient/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    fields = '__all__'
    template_name = 'patient/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient/patient_delete.html'
    success_url = reverse_lazy('patient_list')