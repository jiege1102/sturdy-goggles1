from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=50,default='')
    total_score = models.DecimalField(max_digits=5, decimal_places=1)
    chinese_score = models.DecimalField(max_digits=5, decimal_places=1)
    math_score = models.DecimalField(max_digits=5, decimal_places=1)
    english_score = models.DecimalField(max_digits=5, decimal_places=1)
    physics_score = models.DecimalField(max_digits=5, decimal_places=1)
    average_score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Student_details(models.Model):
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    class_number = models.IntegerField()
    total_score = models.DecimalField(max_digits=5, decimal_places=1)
    class_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    school_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    district_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    chinese_score = models.DecimalField(max_digits=5, decimal_places=1)
    class_chinese_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    school_chinese_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    district_chinese_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    math_score = models.DecimalField(max_digits=5, decimal_places=1)
    class_math_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    school_math_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    district_math_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    english_score = models.DecimalField(max_digits=5, decimal_places=1)
    class_english_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    school_english_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    district_english_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    physics_score = models.DecimalField(max_digits=5, decimal_places=1)
    class_physics_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    school_physics_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    district_physics_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    history_score_one = models.DecimalField(max_digits=5, decimal_places=1)
    history_chinese_score_one = models.DecimalField(max_digits=5, decimal_places=1)
    history_math_score_one = models.DecimalField(max_digits=5, decimal_places=1)
    history_english_score_one = models.DecimalField(max_digits=5, decimal_places=1)
    history_score_two = models.DecimalField(max_digits=5, decimal_places=1)
    history_chinese_score_two = models.DecimalField(max_digits=5, decimal_places=1)
    history_math_score_two = models.DecimalField(max_digits=5, decimal_places=1)
    history_english_score_two = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return self.name


