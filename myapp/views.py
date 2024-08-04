from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, BlogPostForm
from .models import CustomUser, BlogPost

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.is_patient:
                return redirect('patient_dashboard', user_id=user.id)
            elif user.is_doctor:
                return redirect('doctor_dashboard', user_id=user.id)
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

@login_required
def patient_dashboard(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request, 'myapp/patient_dashboard.html', {'user': user})

@login_required
def doctor_dashboard(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    posts = BlogPost.objects.filter(author=user)
    return render(request, 'myapp/doctor_dashboard.html', {'user': user, 'posts': posts})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('doctor_blog_list')  # Redirect to the doctor's blog list
    else:
        form = BlogPostForm()
    return render(request, 'myapp/create_blog_post.html', {'form': form})

@login_required
def doctor_blog_list(request):
    blog_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'myapp/doctor_blog_list.html', {'blog_posts': blog_posts})

def blog_list(request):
    categories = BlogPost.CATEGORIES
    blogs_by_category = {category[0]: BlogPost.objects.filter(category=category[0], is_draft=False) for category in categories}
    return render(request, 'myapp/blog_list.html', {'blogs_by_category': blogs_by_category})
