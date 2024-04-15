import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


url = '/api/v1/courses/'

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses = course_factory(_quantity=1)
    response = client.get(f'{url}{courses[0].id}/')
    data = response.json()
    assert response.status_code == 200
    assert courses[0].name == data.get('name')


@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_fiter_id_course(client, course_factory):
    courses = course_factory(_quantity=10)
    for i, course in enumerate(courses):
        response = client.get(url, data={id: course.id})
        data = response.json()
        assert course.id == data[i]['id']
        assert response.status_code == 200


@pytest.mark.django_db
def test_fiter_name_course(client, course_factory):
    courses = course_factory(_quantity=10)
    for i, course in enumerate(courses):
        response = client.get(url, data={id: course.name})
        data = response.json()
        assert course.name == data[i]['name']
        assert response.status_code == 200


@pytest.mark.django_db
def test_post_course(client):
    response = client.post(url, data={'name': 'course_name'})
    assert response.status_code == 201


@pytest.mark.django_db
def test_put_course(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.patch(f'{url}+{courses[0].id}/', data={'name': 'changed course'})
    data = response.json()
    assert data['name'] == 'changed course'
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.delete(f'{url}+{courses[0].id}/', data={'name': 'changed course'})
    assert response.status_code == 204
