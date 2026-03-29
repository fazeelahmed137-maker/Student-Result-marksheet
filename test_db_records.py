import os
import sys

sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_result_django.settings')
import django
django.setup()

from results.models import Student, Mark

with open("output.txt", "w") as f:
    f.write(f"Total Students: {Student.objects.count()}\n")
    f.write(f"Total Marks: {Mark.objects.count()}\n")

    for s in Student.objects.all()[:5]:
        f.write(f"Student: {s.roll_no} - {s.name} (Dept: {s.department.name}, Year: {s.year.year}, Sem: {s.semester.name})\n")

    for m in Mark.objects.all()[:5]:
        f.write(f"Mark: {m.student.roll_no} - {m.subject.name} - Int:{m.internal} Ext:{m.external}\n")
