from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-Binary'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    student_class = models.IntegerField()
    roll_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    enrollment_date = models.DateField()
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    parent_guardian_name = models.CharField(max_length=60)
    parent_guardian_phone = models.CharField(max_length=15)
    parent_guardian_email = models.EmailField()
    emergency_contact = models.CharField(max_length=60)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True, null=True)
    courses = models.ManyToManyField(Course, through='StudentCourses')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class StudentCourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'course')
