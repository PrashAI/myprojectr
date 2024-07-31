from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('patient_dashboard/<int:user_id>/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/<int:user_id>/', views.doctor_dashboard, name='doctor_dashboard'),
]