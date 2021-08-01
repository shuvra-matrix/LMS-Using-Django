from django.contrib import admin
from lms_app.models import Classes, Create_assignment, Student, Submit, Course, Department, Subject, Teacher, Subject_assign,Admin,Reading_materials

# Register your models here.

admin.site.register(Classes),
admin.site.register(Create_assignment),
admin.site.register(Student),
admin.site.register(Submit),
admin.site.register(Department),
admin.site.register(Course),
admin.site.register(Subject),
admin.site.register(Teacher),
admin.site.register(Subject_assign),
admin.site.register(Admin),
admin.site.register(Reading_materials),
