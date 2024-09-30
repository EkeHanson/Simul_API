from django.contrib import admin
from .models import Jobs


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'requirements', 'start_date', 'start_date')
