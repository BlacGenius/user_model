from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea, TextInput

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff', )
    ordering = ('-start_date', )
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff', )

admin.site.register(NewUser, UserAdminConfig)
