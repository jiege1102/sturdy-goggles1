from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Student_details, Student_evaluate, Chinese, Math, English, Physics
from .serializers import StudentSerializer, Student_detailsSerializer_bar, Student_evaluateSerializer, \
    ChineseSerializer, MathSerializer, EnglishSerializer, PhysicsSerializer
from rest_framework.decorators import api_view

class StudentGradeView(APIView):
    # authentication_classes = [TokenAuthentication]  # 添加TokenAuthentication
    # permission_classes = [IsAuthenticated]  # 添加IsAuthenticated

    def post(self, request):
        # 获取请求数据中的姓名和学校信息
        name = request.data.get('name')
        nume = request.data.get('nume')
        print(name, nume)

        # 根据姓名和学校信息查询学生记录
        try:
            student = Student.objects.get(name=name, nume=nume)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def student_details(request):
    current_user = request.user.username
    try:
        # 查询当前用户的详细信息
        student = Student_details.objects.get(name=current_user)
        serializer = Student_detailsSerializer_bar(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def student_evaluate(request):
    current_user = request.user.username
    try:
        # 查询当前用户的详细信息
        student = Student_evaluate.objects.get(name=current_user)
        serializer = Student_evaluateSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

class ChineseListView(ListAPIView):
    serializer_class = ChineseSerializer

    def get_queryset(self):
        current_user = self.request.user.username
        return Chinese.objects.filter(name=current_user)

class MathListView(ListAPIView):
    serializer_class = MathSerializer

    def get_queryset(self):
        current_user = self.request.user.username
        return Math.objects.filter(name=current_user)

class EnglishListView(ListAPIView):
    serializer_class = EnglishSerializer

    def get_queryset(self):
        current_user = self.request.user.username
        return English.objects.filter(name=current_user)

class PhysicsListView(ListAPIView):
    serializer_class = PhysicsSerializer

    def get_queryset(self):
        current_user = self.request.user.username
        return Physics.objects.filter(name=current_user)