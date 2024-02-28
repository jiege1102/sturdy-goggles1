from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Student_details
from .serializers import StudentSerializer, Student_detailsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class StudentGradeView(APIView):
    # authentication_classes = [TokenAuthentication]  # 添加TokenAuthentication
    # permission_classes = [IsAuthenticated]  # 添加IsAuthenticated

    def post(self, request):
        # 获取请求数据中的姓名和学校信息
        name = request.data.get('name')
        school = request.data.get('school')
        print(name, school)

        # 根据姓名和学校信息查询学生记录
        try:
            student = Student.objects.get(name=name, school=school)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # 添加IsAuthenticated
def student_details(request):
    current_user = request.user.username
    try:
        # 查询当前用户的详细信息
        student = Student_details.objects.get(name=current_user)
        serializer = Student_detailsSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
