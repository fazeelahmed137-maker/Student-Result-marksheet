import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_result_django.settings")
django.setup()

from results.models import Department, Year, Semester, Student, Subject, Mark

dept = Department.objects.first()
year = Year.objects.first()
sem = Semester.objects.first()
sub = Subject.objects.first()
student = Student.objects.first()

print("Initial create with 0 external")
mark, created = Mark.objects.update_or_create(
    student=student, subject=sub, semester=1,
    defaults={"internal": 10, "external": 0}
)
print(f"External: 0 => Result: {mark.result}")

print("Update to 20 external")
mark, created = Mark.objects.update_or_create(
    student=student, subject=sub, semester=1,
    defaults={"internal": 10, "external": 20}
)
print(f"External: 20 => Result: {mark.result}")

print("Update to 40 external")
mark, created = Mark.objects.update_or_create(
    student=student, subject=sub, semester=1,
    defaults={"internal": 10, "external": 40}
)
print(f"External: 40 => Result: {mark.result}")

mark.delete()
