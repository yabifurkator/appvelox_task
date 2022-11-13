import json
from rest_framework.test import APITestCase
from rest_framework import status

from todo.models import Task


class CreateNewTaskEndpointTestCase(APITestCase):
    url = '/new/'
    def test_create_new_task(self):
        task_json = {
            'title': 'test_title',
            'text': 'test_text'
        }
        response = self.client.post(path=self.url, data=task_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)

        obj = Task.objects.last()
        self.assertEqual(obj.title, 'test_title')
        self.assertEqual(obj.text, 'test_text')
        self.assertEqual(obj.completed, False)
        self.assertEqual(obj.completion_date, None)

    def test_wrong_http_method(self):
        task_json = {
            'title': 'test_title',
            'text': 'test_text'
        }
        response = self.client.get(
            path=self.url,
            data=task_json,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Task.objects.count(), 0)

    def test_no_json(self):
        response = self.client.post(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)

    def test_wrong_json_field(self):
        task_json = {
            'TAITL': 'test_title',
            'text': 'test_text'
        }
        response = self.client.post(path=self.url, data=task_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)
        
        task_json = {
            'title': 'test_title',
            'TXT': 'test_text'
        }
        response = self.client.post(path=self.url, data=task_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)

    def test_wrong_json_data(self):
        task_json = {
            'title': '',
            'text': 'test_text'
        }
        response = self.client.post(path=self.url, data=task_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)
    
        task_json = {
            'title': 'title',
            'text': ''
        }
        response = self.client.post(path=self.url, data=task_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)

        task = {
            'title': '',
            'text': ''
        }
        response = self.client.post(path=self.url, data=task_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)
