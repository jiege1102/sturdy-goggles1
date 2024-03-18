from rest_framework import serializers
from .models import Student, Student_details, Student_evaluate,Chinese, Math, English, Physics

class StudentwenjuanSerializer:
    pass


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['nume','name', 'school', 'total_score', 'chinese_score', 'math_score', 'english_score', 'physics_score',
                  'average_score']


class Student_detailsSerializer_bar(serializers.ModelSerializer):
    class Meta:
        model = Student_details
        fields = ['name', 'school', 'class_number', 'total_score', 'class_average_score', 'school_average_score'
            , 'district_average_score', 'chinese_score', 'class_chinese_average_score', 'school_chinese_average_score'
            , 'district_chinese_average_score', 'math_score', 'class_math_average_score', 'school_math_average_score'
            , 'district_math_average_score', 'english_score', 'class_english_average_score',
                  'school_english_average_score'
            , 'district_english_average_score', 'physics_score', 'class_physics_average_score',
                  'school_physics_average_score'
            , 'district_physics_average_score','history_score_one', 'history_chinese_score_one', 'history_math_score_one', 'history_english_score_one',
                  'history_score_two', 'history_chinese_score_two', 'history_math_score_two', 'history_english_score_two']



class Student_detailsSerializer_line(serializers.ModelSerializer):
    class Meta:
        model = Student_details
        fields = ['name', 'school', 'class_number', 'total_score','chinese_score', 'math_score', 'english_score','history_score_one', 'history_chinese_score_one', 'history_math_score_one', 'history_english_score_one',
                  'history_score_two', 'history_chinese_score_two', 'history_math_score_two', 'history_english_score_two']


class Student_evaluateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_evaluate
        fields = '__all__'



class ChineseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chinese
        fields = '__all__'

class MathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Math
        fields = '__all__'

class EnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = '__all__'

class PhysicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physics
        fields = '__all__'