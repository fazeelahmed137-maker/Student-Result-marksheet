from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Year(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.CharField(max_length=20)

    def __str__(self):
        return str(self.year)


class Semester(models.Model):
    name = models.CharField(max_length=20)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    credits = models.IntegerField(default=3)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    semester = models.IntegerField(choices=[
        (1, 'Semester 1'),
        (2, 'Semester 2'),
        (3, 'Semester 3'),
        (4, 'Semester 4'),
        (5, 'Semester 5'),
        (6, 'Semester 6'),
    ])

    class Meta:
        unique_together = ('code', 'department', 'year', 'semester')

    def __str__(self):
        return f"{self.code} - {self.name}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.IntegerField()   # stores the semester number (1-6)

    internal = models.IntegerField()
    external = models.IntegerField()

    is_cleared = models.BooleanField(default=False)
    total = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=1, blank=True)

    def save(self, *args, **kwargs):
        if self.internal > 25:
            raise ValueError("Internal must be ≤ 25")

        if self.external > 75:
            raise ValueError("External must be ≤ 75")

        if self.external == 0:
            self.result = 'A'
            self.is_cleared = False
        elif 1 <= self.external <= 29:
            self.result = 'F'
            self.is_cleared = False
        else:
            self.result = 'P'
            self.is_cleared = True

        self.total = self.internal + self.external
        super().save(*args, **kwargs)
