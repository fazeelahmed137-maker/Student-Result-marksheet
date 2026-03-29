import os
import sys
import django
import random

sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_result_django.settings')
django.setup()

from results.models import Department, Year, Semester, Subject, Student, Mark

# --- Names ---
hindu_names = ["Aarav", "Advait", "Arjun", "Karthik", "Kavya", "Pranav", "Riya", "Rohan", "Siddharth", "Vivek", "Vishal", "Yash", "Aditya", "Akash", "Deepak", "Hari", "Kiran", "Manish", "Gowtham", "Srinivas", "Venkatesh", "Balaji", "Nanda", "Aaditya", "Krishnan", "Aaradhya", "Ananya", "Nikhila", "Swamika", "Bhavya", "Gowri", "Isha", "Lakshmi", "Priya", "Sandhya", "Sneha", "Nithya"]
muslim_names = ["Aamir", "Abdul", "Bilal", "Hassan", "Ibrahim", "Mohammed", "Omar", "Rizwan", "Tariq", "Umar", "Zain", "Ali", "Hussain", "Imran", "Salman", "Tahir", "Numan", "Jalal", "Usman", "Ayesha", "Fatima", "Jamila", "Khadija", "Nadia", "Sana", "Zainab", "Mariam", "Salma", "Yasmin"]
christian_names = ["Aaron", "Caleb", "Daniel", "David", "Isaac", "Jacob", "John", "Joseph", "Joshua", "Luke", "Matthew", "Michael", "Paul", "Peter", "Samuel", "Stephen", "Thomas", "Antony", "Jeremiah", "Abigail", "Chloe", "Elizabeth", "Esther", "Hannah", "Mary", "Rebecca", "Ruth", "Sarah", "Grace"]

NO_ARREAR_SUBJECTS = ["U18CEA601", "U18MCAP60", "U18EINP51"]

def get_random_name():
    category = random.choices(["hindu", "muslim", "christian"], weights=[60, 20, 20])[0]
    if category == "hindu":
        return random.choice(hindu_names)
    elif category == "muslim":
        return random.choice(muslim_names)
    else:
        return random.choice(christian_names)

def generate_mark(subject, is_arrear=False, is_absent=False):
    # If this subject is exempt from arrears, force pass
    if subject.code in NO_ARREAR_SUBJECTS:
        is_arrear = False
        is_absent = False
        
    if is_absent:
        return 0, 0
    elif is_arrear:
        # Internal out of 25, external out of 75. Pass is >= 30 in external.
        internal = random.randint(10, 25)
        external = random.randint(0, 29)
        return internal, external
    else:
        internal = random.randint(15, 25)
        external = random.randint(30, 75)
        return internal, external

def generate_students(dept_id, year_id, current_sem, prefix, count=50):
    department = Department.objects.get(id=dept_id)
    year_obj = Year.objects.get(id=year_id)
    
    # Get or create the current semester for the student profile
    semester_obj, _ = Semester.objects.get_or_create(year=year_obj, name=str(current_sem))
    
    students = []
    # If starting from 1 to count
    for i in range(1, count + 1):
        roll_no = f"{prefix}{i:02d}"
        name = get_random_name()
        dob = f"{random.randint(2000, 2005)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        
        student, _ = Student.objects.update_or_create(
            roll_no=roll_no,
            defaults={
                "name": name,
                "dob": dob,
                "department": department,
                "year": year_obj,
                "semester": semester_obj
            }
        )
        students.append(student)
        
    return students, department, year_obj

def generate_marks_for_students(students, department, up_to_sem):
    subjects_by_sem = {}
    for sem in range(1, up_to_sem + 1):
        subjects = list(Subject.objects.filter(department=department, semester=sem))
        subjects_by_sem[sem] = subjects

    for student in students:
        active_arrears = [] # list of (subject, orig_sem)
        
        for sem in range(1, up_to_sem + 1):
            # Attempt to clear active arrears in this semester
            cleared_arrears = []
            for arr_subj, orig_sem in active_arrears:
                # 80% chance to clear arrear each subsequent semester
                if random.random() < 0.8:
                    v_int, v_ext = generate_mark(arr_subj, is_arrear=False)
                    Mark.objects.update_or_create(
                        student=student, subject=arr_subj, semester=sem,
                        defaults={"internal": v_int, "external": v_ext}
                    )
                    cleared_arrears.append((arr_subj, orig_sem))
                else:
                    # Still failing
                    v_int, v_ext = generate_mark(arr_subj, is_arrear=True)
                    Mark.objects.update_or_create(
                        student=student, subject=arr_subj, semester=sem,
                        defaults={"internal": v_int, "external": v_ext}
                    )
                    
            for ca in cleared_arrears:
                active_arrears.remove(ca)

            # Generate marks for current semester regular subjects
            for subject in subjects_by_sem[sem]:
                # 15% chance of arrear, 5% chance of absent, 80% pass
                r = random.random()
                
                # Check exempt subjects
                if subject.code in NO_ARREAR_SUBJECTS:
                    is_arrear = False
                    is_absent = False
                else:
                    is_arrear = r < 0.15
                    is_absent = 0.15 <= r < 0.20
                    
                v_int, v_ext = generate_mark(subject, is_arrear=is_arrear, is_absent=is_absent)
                Mark.objects.update_or_create(
                    student=student, subject=subject, semester=sem,
                    defaults={"internal": v_int, "external": v_ext}
                )
                
                if is_arrear or is_absent:
                    active_arrears.append((subject, sem))

def main():
    dept_id = 4  # Bsc Chemistry
    
    print(f"Generating 1st Year (Sem 1) for Dept {dept_id}...")
    y1_students, dept, _ = generate_students(dept_id, 10, 1, "HCU23A", 60)
    generate_marks_for_students(y1_students, dept, 1)

    print(f"Generating 2nd Year (Sem 3) for Dept {dept_id}...")
    y2_students, dept, _ = generate_students(dept_id, 11, 3, "HCU22A", 60)
    generate_marks_for_students(y2_students, dept, 3)

    print(f"Generating 3rd Year (Sem 5) for Dept {dept_id}...")
    y3_students, dept, _ = generate_students(dept_id, 12, 5, "HCU21A", 60)
    generate_marks_for_students(y3_students, dept, 5)

    print("Done! Total Students in DB:", Student.objects.count())
    print("Total Marks in DB:", Mark.objects.count())

if __name__ == "__main__":
    main()
