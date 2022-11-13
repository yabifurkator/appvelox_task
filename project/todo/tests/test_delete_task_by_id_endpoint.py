import json
from datetime import datetime
from rest_framework.test import APITestCase
from rest_framework import status

from todo.models import Task


class DeleteTaskByIdEndpointTestCase(APITestCase):
    url = '/delete/'
    def setUp(self):
        Task(title='test_title1', text='test_text1').save()
        Task(title='test_title2', text='test_text2').save()
        Task(title='test_title3', text='test_text3').save()

    def test_delete_taks_by_id(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 3)
        self.assertEqual(tasks[0].pk, 1)
        self.assertEqual(tasks[1].pk, 2)
        self.assertEqual(tasks[2].pk, 3)

        data_json = {'pk': 2}
        response = self.client.post(
            path=self.url,
            data=data_json,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRaises(Task.DoesNotExist, Task.objects.get, pk=2)
        self.assertEqual(Task.objects.count(), 2)

    def test_delete_nonexistent_task(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 3)
        self.assertEqual(tasks[0].pk, 1)
        self.assertEqual(tasks[1].pk, 2)
        self.assertEqual(tasks[2].pk, 3)

        data_json = {'pk': 4}
        response = self.client.post(
            path=self.url,
            data=data_json,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Task.objects.count(), 3)

    def test_wrong_http_method(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 3)
        self.assertEqual(tasks[0].pk, 1)
        self.assertEqual(tasks[1].pk, 2)
        self.assertEqual(tasks[2].pk, 3)
        
        data_json = {'pk': 2}
        response = self.client.generic(
            method='GET',
            path=self.url,
            data=json.dumps(data_json),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
