from django.contrib import admin
from .models import Department, Year, Subject, Student, Mark, Semester

admin.site.register(Year)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Mark)
admin.site.register(Department)
admin.site.register(Semester)
