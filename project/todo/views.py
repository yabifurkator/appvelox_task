import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .models import Task


def index(request):
    return HttpResponse('Hello, ToDo!')


def get_all_tasks(request):
    tasks = Task.objects.all()
    tasks_json = serializers.serialize(format='json', queryset=tasks)
    return JsonResponse(tasks_json, safe=False)


@csrf_exempt
def create_new_task(request):
    task_fields = json.loads(json.loads(request.body))
    title = task_fields['title']
    text = task_fields['text']

    task = Task(
        title=title,
        text=text
    )
    task.save()

    return HttpResponse()


def get_task_by_id(request):
    pk = json.loads(json.loads(request.body))['pk']
    task = Task.objects.get(pk=pk)
    task_json = serializers.serialize(format='json', queryset=[task])
    return JsonResponse(task_json, safe=False)


@csrf_exempt
def complete_task_by_id(request):
    pk = json.loads(json.loads(request.body))['pk']
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return HttpResponse()


@csrf_exempt
def delete_task_by_id(request):
    pk = json.loads(json.loads(request.body))['pk']
    task = Task.objects.get(pk=pk)
    task.delete()
    return HttpResponse()
