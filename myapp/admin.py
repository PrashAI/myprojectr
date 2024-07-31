from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_patient', 'is_doctor', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)