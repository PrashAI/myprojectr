from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser 
import logging
logger = logging.getLogger(__name__)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                user = form.save()
                print('USER : \n', user)
                login(request, user)
                # Redirect based on user type, assuming these methods exist
                if hasattr(user, 'is_patient') and user.is_patient:
                    return redirect('patient_dashboard', user_id=user.id)
                elif hasattr(user, 'is_doctor') and user.is_doctor:
                    return redirect('doctor_dashboard', user_id=user.id)
                else:
                    return redirect('signup')  # Or some other default page
            else:
                logger.error(f"Form errors: {form.errors}")

        except Exception as e:
            print(e)
            return render(request, 'myapp/signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

@login_required
def patient_dashboard(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not user.is_patient:
        return redirect('signup')  # Redirect if user is not a patient
    return render(request, 'myapp/patient_dashboard.html', {'user': user})

@login_required
def doctor_dashboard(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not user.is_doctor:
        return redirect('signup')  # Redirect if user is not a doctor
    return render(request, 'myapp/doctor_dashboard.html', {'user': user})