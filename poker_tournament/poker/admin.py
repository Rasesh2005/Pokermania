from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        # ('Google Details', {
        #     'fields': ('google_id', 'profile_picture'),
        # }),
    )
    # list_display = ['username', 'email', 'google_id']
    list_display = ['username', 'email']