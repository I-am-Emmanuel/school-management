from django.db import models

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
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=11, unique=True)
    relationship = models.CharField(max_length=8, choices=RELATIONSHIP_CHOICES)
    address = models.CharField(max_length=250)
    profile_pics = models.ImageField(upload_to='profile_image', blank=False,)

class Classroom(models.Model):
    class_name = models.CharField(max_length=30)

class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    profile_pics = models.ImageField(upload_to='profile_image', blank=False)

class StaffModel(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=11, unique=True)
    teaching_staff = models.BooleanField()
    profile_pics = models.ImageField()


class Subject(models.Model):
    pass


# for i in range(100):
#     if i % 3 == 0 and i % 15 == 0:
#         print('goat')
#     elif i % 3 == 0:
#         print('dog')
#     else:
#         print(i)