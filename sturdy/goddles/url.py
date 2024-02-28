from django.urls import path
from .views import StudentGradeView, student_details

urlpatterns = [
    path('my-grade/', StudentGradeView.as_view(), name='my_grade'),
    path('student_details/', student_details, name='student_details'),
]
