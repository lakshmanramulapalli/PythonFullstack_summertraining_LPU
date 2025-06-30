from django.urls import path
from .views import (
    PatientListView, PatientDetailView,
    PatientCreateView, PatientUpdateView, PatientDeleteView
)

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patient/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name='patient_update'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
]
