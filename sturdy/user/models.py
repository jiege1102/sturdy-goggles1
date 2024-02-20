from django.contrib.auth.models import AbstractUser
from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(AbstractUser):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)
    groups = models.ManyToManyField('auth.Group', related_name='students_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='students_permissions')

    def __str__(self):
        return self.username

class Teacher(AbstractUser):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)
    groups = models.ManyToManyField('auth.Group', related_name='teachers_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='teachers_permissions')

    def __str__(self):
        return self.username
