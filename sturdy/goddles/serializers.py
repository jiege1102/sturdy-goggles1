from rest_framework import serializers
from .models import Student, Student_details


class StudentwenjuanSerializer:
    pass


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'school', 'total_score', 'chinese_score', 'math_score', 'english_score', 'physics_score',
                  'average_score']


class Student_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_details
        fields = ['name', 'school', 'class_number', 'total_score', 'class_average_score', 'school_average_score'
            , 'district_average_score', 'chinese_score', 'class_chinese_average_score', 'school_chinese_average_score'
            , 'district_chinese_average_score', 'math_score', 'class_math_average_score', 'school_math_average_score'
            , 'district_math_average_score', 'english_score', 'class_english_average_score',
                  'school_english_average_score'
            , 'district_english_average_score', 'physics_score', 'class_physics_average_score',
                  'school_physics_average_score'
            , 'district_physics_average_score']
