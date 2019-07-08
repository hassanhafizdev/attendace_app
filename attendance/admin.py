from django.contrib import admin

from .models import(
    Gender, Teacher, Student, StudentAttendance, TeacherAttendace
)
# Register your models here.

admin.site.register(Gender)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentAttendance)
admin.site.register(TeacherAttendace)