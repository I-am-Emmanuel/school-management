from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ParentOrGuardianModel(models.Model):
    FATHER = 'father'
    MOTHER = 'mother'
    GUARDIAN = 'guardian'

    RELATIONSHIP_CHOICES = [
        ('FATHER', 'father'),
        ('MOTHER', 'mother'),
        ('GUARDIAN', 'guardian'),
    ]
    # first_name = models.CharField(max_length=50, null=False)
    # last_name = models.CharField(max_length=50, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, unique=True)
    relationship = models.CharField(max_length=8, choices=RELATIONSHIP_CHOICES)
    address = models.CharField(max_length=250)
    profile_pics = models.ImageField(upload_to='profile_image', blank=False,)

    def __str__(self):
        return self.user.last_name

class Classroom(models.Model):
    class_name = models.CharField(max_length=30)

class Subject(models.Model):
    pass

class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    profile_pics = models.ImageField(upload_to='profile_image', blank=False)
    classroom = models.ForeignKey(Classroom, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class StaffModel(models.Model):
    # first_name = models.CharField(max_length=50, null=False)
    # last_name = models.CharField(max_length=50, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, unique=True)
    teaching_staff = models.BooleanField()
    profile_pics = models.ImageField()

    def __str__(self):
        return self.user.last_name





# for i in range(100):
#     if i % 3 == 0 and i % 15 == 0:
#         print('goat')
#     elif i % 3 == 0:
#         print('dog')
#     else:
#         print(i)