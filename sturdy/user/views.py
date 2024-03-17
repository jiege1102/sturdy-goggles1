# user/views.py
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer, MyTokenRefreshSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not (username and password):
            return Response({'error': 'Please provide username, password'}, status=400)
        # 验证用户
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=400)

        # 生成JWT令牌
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            # 'school': user.school.name if user.school else '',
        })


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 校验角色是否有效
        role = serializer.validated_data.get('role')
        if role not in ['student', 'teacher']:
            return Response({'error': 'Invalid role'}, status=status.HTTP_400_BAD_REQUEST)

        # 创建用户并设置密码
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password'))
        user.save()

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
