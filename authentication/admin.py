from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import MyUser  # Import your custom user model

class MyUserAdmin(UserAdmin):
    # Specify the fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')

    # Define fieldsets to customize the layout of the user form in the admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'career_interests')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Role info'), {'fields': ('role',)}),  # Add role field here
    )

    # Add additional fields when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'career_interests'),
        }),
    )

    # Use the default UserAdmin method for saving user passwords
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If this is a new user
            obj.set_password(form.cleaned_data['password1'])
        super().save_model(request, obj, form, change)

# Register the custom user model and the custom admin class
admin.site.register(MyUser, MyUserAdmin)
