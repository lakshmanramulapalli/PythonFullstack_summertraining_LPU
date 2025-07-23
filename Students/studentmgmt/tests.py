import pytest
from django.urls import reverse

from studentmgmt.models import Student

#@pytest.mark.django_db
def test_student_create(client):
    response = client.post(reverse('students_create'), {
        'roll_number': 101,
        'name': 'Alice',
        'age': 20
    })
    assert response.status_code == 302  # Redirect after POST
    assert Student.objects.filter(roll_number=101).exists()

    @pytest.mark.django_db
    def test_students_list_view(client):
        Student.objects.create(roll_number=102, name='Bob', age=21)
        response = client.get(reverse('students_list'))
        assert response.status_code == 200
        assert b'Bob' in response.content