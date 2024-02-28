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

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='customuser_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_permissions')

    def __str__(self):
        return self.username


class Studentwenjuan(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    motivation_to_learn = models.IntegerField()
    motivation_evaluation = models.CharField(max_length=50)
    school_motivation_avg = models.FloatField()
    class_motivation_avg = models.FloatField()
    district_motivation_avg = models.FloatField()
    moral_development = models.CharField(max_length=50)
    labor_and_social_practice = models.CharField(max_length=50)
    physical_and_mental_development = models.CharField(max_length=50)
    aesthetic_literacy = models.CharField(max_length=50)
    academic_development = models.CharField(max_length=50)
    current_score = models.FloatField()
    current_score_grade = models.CharField(max_length=50)
    class_avg_score = models.FloatField()
    school_avg_score = models.FloatField()
    district_avg_score = models.FloatField()
    knowledge_internalization = models.CharField(max_length=50)
    chinese_score = models.FloatField()
    chinese_score_evaluation = models.CharField(max_length=50)
    class_avg_chinese_score = models.FloatField()
    school_avg_chinese_score = models.FloatField()
    district_avg_chinese_score = models.FloatField()
    math_score = models.FloatField()
    math_score_evaluation = models.CharField(max_length=50)
    class_avg_math_score = models.FloatField()
    school_avg_math_score = models.FloatField()
    district_avg_math_score = models.FloatField()
    english_score = models.FloatField()
    english_score_evaluation = models.CharField(max_length=50)
    class_avg_english_score = models.FloatField()
    school_avg_english_score = models.FloatField()
    district_avg_english_score = models.FloatField()
    physics_score = models.FloatField()
    physics_score_evaluation = models.CharField(max_length=50)
    class_avg_physics_score = models.FloatField()
    school_avg_physics_score = models.FloatField()
    district_avg_physics_score = models.FloatField()
    history_score_1 = models.FloatField()
    history_chinese_score_1 = models.FloatField()
    history_math_score_1 = models.FloatField()
    history_english_score_1 = models.FloatField()
    history_score_2 = models.FloatField()
    history_chinese_score_2 = models.FloatField()
    history_math_score_2 = models.FloatField()
    history_english_score_2 = models.FloatField()
    cognitive_intensity = models.FloatField()
    cognitive_intensity_evaluation = models.CharField(max_length=50)
    class_cognitive_intensity = models.FloatField()
    school_cognitive_intensity = models.FloatField()
    district_cognitive_intensity = models.FloatField()

    def __str__(self):
        return self.user.username
