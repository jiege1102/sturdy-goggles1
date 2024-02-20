# user/urls.py
from django.urls import path
from .views import CreateStudentView, CreateTeacherView, MyTokenObtainPairView, MyTokenRefreshView

urlpatterns = [
    path('register/student/', CreateStudentView.as_view(), name='register_student'),
    path('register/teacher/', CreateTeacherView.as_view(), name='register_teacher'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]
