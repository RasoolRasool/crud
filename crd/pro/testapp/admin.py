from django.contrib import admin
from testapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['username','password','name','salary','address']

admin.site.register(Employee,EmployeeAdmin)