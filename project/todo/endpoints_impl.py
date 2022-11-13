import json
from datetime import datetime

from django.core import serializers
from django.http import \
    HttpResponse, \
    JsonResponse

from .models import Task

from .tools import \
    todo_response


def get_all_tasks_endpoint_impl(request):
    tasks = Task.objects.all()
    tasks_json = serializers.serialize(format='json', queryset=tasks)
    json_response = JsonResponse(
        status=200,
        data=tasks_json,
        safe=False
    )
    return todo_response(
        response=json_response,
        message='all tasks listed'
    )


def create_new_task_endpoint_impl(request):
    task_fields = json.loads(json.loads(request.body))
    title = task_fields['title']
    text = task_fields['text']

    task = Task(
        title=title,
        text=text
    )
    task.save()

    return todo_response(
        response=HttpResponse(status=200),
        message='new ask added'
    )


def get_task_by_id_endpoint_impl(request):
    pk = json.loads(json.loads(request.body))['pk']
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return todo_response(
            response=HttpResponse(status=404),
            message='task with id={} does not exist'.format(pk)
        )

    task_json = serializers.serialize(format='json', queryset=[task])
    response = JsonResponse(
        status=200,
        data=task_json,
        safe=False
    )
    return todo_response(
        response=response,
        message='task with id={} found'.format(pk)
    )


def complete_task_by_id_endpoint_impl(request):
    json_object = json.loads(json.loads(request.body))
    pk = json_object['pk']
    completion_date = json_object['completion_date']
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return todo_response(
            response=HttpResponse(status=404),
            message='task with id={} does not exist'.format(pk)
        )
        
    if task.completed:
        return todo_response(
            response=HttpResponse(status=403),
            message='task with id={} already completed'.format(pk)
        )
    
    task.completed = True
    task.completion_date = datetime.strptime(completion_date, '%d-%m-%Y')
    task.save()
    return todo_response(
        response=HttpResponse(status=200),
        message='task with id={} completed'.format(pk)
    )


def delete_task_by_id_endpoint_impl(request):
    pk = json.loads(json.loads(request.body))['pk']
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return todo_response(
            response=HttpResponse(status=404),
            message='task with id={} does not exist'.format(pk)
        )
    task.delete()
    return todo_response(
        response=HttpResponse(status=200),
        message='task with id={} deleted'.format(pk)
    )
