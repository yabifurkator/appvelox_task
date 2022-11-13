import json
from django.core import serializers
from rest_framework.test import \
    APITestCase, \
    APIRequestFactory
from rest_framework import status

from todo.models import Task


class GetTaskByIdEndpointTestCase(APITestCase):
    url = '/get/'
    def setUp(self):
        Task(title='test_title1', text='test_text1').save()
        Task(title='test_title2', text='test_text2').save()
        Task(title='test_title3', text='test_text3').save()

    def test_get_taks_by_id(self):
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            list(serializers.deserialize('json', response.json()))[0].object.pk
        except:
            self.fail('Exeption was!')
    
        deserialized_object = serializers.deserialize('json', response.json())
        deserialized_list = list(deserialized_object)
        self.assertEqual(len(deserialized_list), 1)
        task = deserialized_list[0].object

        self.assertEqual(task.pk, 2)
        self.assertEqual(task.title, 'test_title2')
        self.assertEqual(task.text, 'test_text2')

    def test_get_nonexistent_tast(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 3)
        self.assertEqual(tasks[0].pk, 1)
        self.assertEqual(tasks[1].pk, 2)
        self.assertEqual(tasks[2].pk, 3)

        data_json = {'pk': 4}
        response = self.client.generic(
            method='GET',
            path=self.url,
            data=json.dumps(data_json),
            content_type='application/json'
        )
        self.assertRaises(Task.DoesNotExist, Task.objects.get, pk=4)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_wrong_http_method(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 3)
        self.assertEqual(tasks[0].pk, 1)
        self.assertEqual(tasks[1].pk, 2)
        self.assertEqual(tasks[2].pk, 3)

        data_json = {'pk': 2}
        response = self.client.generic(
            method='POST',
            path=self.url,
            data=json.dumps(data_json),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)    
