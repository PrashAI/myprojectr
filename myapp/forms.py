from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, BlogPost

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'is_patient', 'is_doctor', 'profile_picture',
            'address_line1', 'city', 'state', 'pincode'
        )

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
