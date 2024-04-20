from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Adult

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'password1', 'password2'),
        }),
    )
    
admin.site.register(User, CustomUserAdmin) 
admin.site.register(Adult)
