import os, sys, django
# Setup Django
sys.path.append(r'C:\Users\ELCOT\Downloads\student_result_django\student_result_django')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_result_django.settings')
django.setup()

from django.test import Client
from results.models import Department, Year, Semester, Subject

# Create prerequisites for the sample_marks.xlsx
dept, _ = Department.objects.get_or_create(code="CS", defaults={"name": "Computer Science"})
year, _ = Year.objects.get_or_create(name="Year 1")
sem, _ = Semester.objects.get_or_create(year=year, name="1")

# Make subjects match "Tamil", "English", "Maths" as implied by the Excel
Subject.objects.get_or_create(department=dept, semester=sem, code="TAM", defaults={"name": "Tamil", "max_internal": 25, "max_external": 75, "min_pass_external": 30, "min_pass_total": 45, "credits": 3})
Subject.objects.get_or_create(department=dept, semester=sem, code="ENG", defaults={"name": "English", "max_internal": 25, "max_external": 75, "min_pass_external": 30, "min_pass_total": 45, "credits": 3})
Subject.objects.get_or_create(department=dept, semester=sem, code="MAT", defaults={"name": "Maths", "max_internal": 25, "max_external": 75, "min_pass_external": 30, "min_pass_total": 45, "credits": 4})

# Make fake students so marks can attach
from results.models import Student
Student.objects.get_or_create(roll_no="21CS001", department=dept, year=year, defaults={"name": "John Doe", "dob": "2000-01-01"})
Student.objects.get_or_create(roll_no="21CS002", department=dept, year=year, defaults={"name": "Jane Smith", "dob": "2000-01-01"})

client = Client()

with open(r'C:\Users\ELCOT\Downloads\sample_marks.xlsx', 'rb') as f:
    response = client.post('/import-marks/upload/', {
        'excel_file': f,
        'department': dept.id,
        'year': year.id,
        'semester': sem.name
    })

with open('response_output.html', 'wb') as f:
    f.write(response.content)

print(f"Status: {response.status_code}")
