from django.urls import path
from .views import StudentGradeView, student_details, student_evaluate, ChineseListView, EnglishListView, MathListView, \
    PhysicsListView

urlpatterns = [
    path('my-grade/', StudentGradeView.as_view(), name='my_grade'),
    path('student_details/', student_details, name='student_details'),
    path('student_evaluate/', student_evaluate, name='student_evaluate'),
    path('chinese/', ChineseListView.as_view(), name='chinese_list'),
    path('math/', MathListView.as_view(), name='math_list'),
    path('english/', EnglishListView.as_view(), name='english_list'),
    path('physics/', PhysicsListView.as_view(), name='physics_list'),
]

