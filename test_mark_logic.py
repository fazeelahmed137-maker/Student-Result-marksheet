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

if not student:
    student = Student.objects.create(name="Test", roll_no="TMP", dob="2000-01-01", department=dept, year=year, semester=sem)

# TEST 1: ABSENT
m1 = Mark(student=student, subject=sub, semester=1, internal=10, external=0)
m1.save()
print(f"External: 0 => Result: {m1.result}, Cleared: {m1.is_cleared}")
m1.delete()

# TEST 2: ARREAR
m2 = Mark(student=student, subject=sub, semester=1, internal=10, external=15)
m2.save()
print(f"External: 15 => Result: {m2.result}, Cleared: {m2.is_cleared}")
m2.delete()

# TEST 3: PASS
m3 = Mark(student=student, subject=sub, semester=1, internal=10, external=30)
m3.save()
print(f"External: 30 => Result: {m3.result}, Cleared: {m3.is_cleared}")
m3.delete()
