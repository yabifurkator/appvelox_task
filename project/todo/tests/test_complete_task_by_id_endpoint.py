import json
from datetime import datetime
from django.core import serializers
from rest_framework.test import APITestCase
from rest_framework import status

from todo.models import Task


class CompleteTaskByIdEndpointTestCase(APITestCase):
    url = '/complete/'
    def setUp(self):
        Task(title='test_title1', text='test_text1').save()
        Task(title='test_title2', text='test_text2').save()
        Task(title='test_title3', text='test_text3').save()

    def test_complete_taks_by_id(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 3)
        self.assertEqual(tasks[0].pk, 1)
        self.assertEqual(tasks[1].pk, 2)
        self.assertEqual(tasks[2].pk, 3)

        data_json = {
            'pk': 2,
            'completion_date': datetime.now().strftime('%d-%m-%Y')
        }
        response = self.client.post(
            path=self.url,
            data=data_json,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = Task.objects.get(pk=2)
        self.assertEqual(task.pk, 2)
        self.assertEqual(task.title, 'test_title2')
        self.assertEqual(task.text, 'test_text2')
        self.assertEqual(task.completed, True)

        today_date = datetime.today()
        self.assertEqual(task.completion_date.day, today_date.day)
        self.assertEqual(task.completion_date.month, today_date.month)
        self.assertEqual(task.completion_date.year, today_date.year)


    def test_wrong_http_method(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 3)
        self.assertEqual(tasks[0].pk, 1)
        self.assertEqual(tasks[1].pk, 2)
        self.assertEqual(tasks[2].pk, 3)
        
        data_json = {
            'pk': 2,
            'completion_date': datetime.now().strftime('%d-%m-%Y')
        }
        response = self.client.generic(
            method='GET',
            path=self.url,
            data=json.dumps(data_json),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
