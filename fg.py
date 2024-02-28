import requests

def test_student_grade_view():
    # 定义测试数据
    test_data = {'name': 'text1'}

    # 发送 POST 请求
    response = requests.post('http://localhost:8000/goddles/student-grade/', json=test_data)

    # 验证响应状态码是否为 200
    assert response.status_code == 200

    # 解析响应数据
    data = response.json()

    # 验证返回的数据是否包含正确的信息
    assert data['name'] == 'John Doe'
    # 继续验证其他字段...

if __name__ == "__main__":
    test_student_grade_view()
