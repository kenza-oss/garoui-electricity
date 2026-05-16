from django.contrib import admin
from .models import Employee, EmployeeWorkImage

class EmployeeWorkImageInline(admin.TabularInline):
    model = EmployeeWorkImage
    extra = 1

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'address')
    search_fields = ('first_name', 'last_name', 'role')
    inlines = [EmployeeWorkImageInline]
