from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Career  # Import your Career model

# Register your models here.


# User = get_user_model()

class CareerAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin list view
    list_display = ('title', 'qualifications', 'job_outlook')

    # Add search functionality for easier lookup
    search_fields = ('title', 'qualifications')

    # Optional: Customize the form layout for detailed view
    fieldsets = (
        (None, {'fields': ('title', 'description')}),
        ('Details', {'fields': ('qualifications', 'job_outlook', 'pathways')}),
    )

# Register the Career model with the custom admin class
admin.site.register(Career, CareerAdmin)

# admin.site.register(User)