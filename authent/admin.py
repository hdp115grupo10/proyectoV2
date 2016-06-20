from django.contrib import admin
from django.contrib.auth.models import User
from .models import Department,Employee
from django.contrib.auth.admin import UserAdmin

class EmployeeInline(admin.TabularInline):
    model=Employee



class DepartmentAdmin(admin.ModelAdmin):
    fieldsets=(
        ("Department information", {
            'fields':('dep_code','dep_name',),
            }),
        )
    list_display=('dep_code','dep_name')

admin.site.register(Department, DepartmentAdmin)
UserAdmin.inlines+=[EmployeeInline,]
UserAdmin.list_display +=('id',)
