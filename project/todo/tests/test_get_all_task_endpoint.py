from django.core import serializers
from rest_framework.test import APITestCase
from rest_framework import status

from todo.models import Task


class GetAllTaskEndpointTestCase(APITestCase):
    url = '/all/'
    def test_empty_database(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), '[]')
    
    def test_wrong_http_method(self):
        response = self.client.post(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_one_task(self):
        task = Task(title='test_title', text='test_text')
        task.save()
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            serializers.serialize(format='json', queryset=[task])
        )

    def test_two_tasks(self):
        task1, task2 = [
            Task(title='test_title1', text='test_text1'),
            Task(title='test_tiele2', text='test_title2')
        ]
        task1.save()
        task2.save()
    
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            serializers.serialize(format='json', queryset=[task1, task2])
        )
    