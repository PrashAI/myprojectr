from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('patient_dashboard/<int:user_id>/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/<int:user_id>/', views.doctor_dashboard, name='doctor_dashboard'),
    path('create_blog_post/', views.create_blog_post, name='create_blog_post'),
    path('doctor_blog_list/', views.doctor_blog_list, name='doctor_blog_list'),  # URL for doctor's blog list
    path('blog_list/', views.blog_list, name='blog_list'),
]