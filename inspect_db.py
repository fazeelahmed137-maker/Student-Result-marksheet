import os
import sys
import django

sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_result_django.settings')
django.setup()

from results.models import Department, Year, Semester, Subject

with open("inspect_out.txt", "w", encoding="utf-8") as f:
    f.write("--- Departments ---\n")
    for d in Department.objects.all():
        f.write(f"ID: {d.id}, Name: {d.name}\n")

    f.write("\n--- Years ---\n")
    for y in Year.objects.all():
        f.write(f"ID: {y.id}, Dept ID: {y.department_id}, Year: {y.year}\n")

    f.write("\n--- Semesters ---\n")
    for s in Semester.objects.all():
        f.write(f"ID: {s.id}, Year ID: {s.year_id}, Name: {s.name}\n")

    f.write("\n--- Subjects ---\n")
    for s in Subject.objects.all():
        f.write(f"ID: {s.id}, Dept ID: {s.department_id}, Sem: {s.semester}, Code: {s.code}, Name: {s.name}\n")
