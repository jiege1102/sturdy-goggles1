from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class TestStudentViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # 创建一个测试用户
        self.user = User.objects.create_user(username='邵俊喆', password='123456')

    def test_login_and_query_student(self):
        # 测试登录
        login_data = {"username": "邵俊喆", "password": "123456"}
        login_response = self.client.post('/login/', login_data)
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.assertIn('access', login_response.data)

        # 提取访问令牌
        token = login_response.data['access']

        # 使用访问令牌进行查询
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        query_data = {"name": "邵俊喆", "school": "Test School"}
        query_response = self.client.post('/student-grade/', query_data)
        self.assertEqual(query_response.status_code, status.HTTP_200_OK)
        self.assertIn('student', query_response.data)
        self.assertIn('details', query_response.data)

        # 检查查询结果
        student_data = query_response.data['student']
        self.assertEqual(student_data['name'], '邵俊喆')
        # 添加其他必要的断言，检查学生的其他信息

if __name__ == '__main__':
    import unittest
    unittest.main()
