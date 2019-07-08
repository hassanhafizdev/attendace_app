from django.db import models

# Create your models here.

class Gender(models.Model):
    male = models.CharField(max_length=1)
    female = models.CharField(max_length=1)

class Person(models.Model):
    first = models.CharField(max_length = 30)
    last = models.CharField(max_length = 30)
    date_of_birth = models.DateField(name='Date of birth')
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=False)
    cnic = models.CharField(max_length=13, primary_key=True)

    def __str__(self):
        return f"{self.first} {self.last}"

class Teacher(Person):
    pass

class Student(Person):
    pass

class Attendance(models.Model):
    attendace_date = models.DateField(name='Attendance for')
    is_present = models.BooleanField()

    def __str__(self):
        return 'Present' if self.is_present else 'Absent'

class StudentAttendance(Attendance):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class TeacherAttendace(Attendance):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)