from django.contrib import admin
from .models import Teacher, Employee

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("username","firstname", "lastname", "mobile","email")

admin.site.register(Teacher, TeacherAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("emp_id","emp_fname","emp_lname","emp_dept","emp_city")

admin.site.register( Employee, EmployeeAdmin)