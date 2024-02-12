from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    total_score = models.DecimalField(max_digits=5, decimal_places=1)
    chinese_score = models.DecimalField(max_digits=5, decimal_places=1)
    math_score = models.DecimalField(max_digits=5, decimal_places=1)
    english_score = models.DecimalField(max_digits=5, decimal_places=1)
    physics_score = models.DecimalField(max_digits=5, decimal_places=1)
    average_score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
