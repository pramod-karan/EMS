from django.contrib import admin
from emp_app.models import Employee, Role, Department, Contact

# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Contact)