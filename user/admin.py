from django.contrib import admin

from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'full_name', 'is_active', 'is_admin')
    search_fields = ('email', 'username', 'full_name')
    ordering = ('email',)
    
