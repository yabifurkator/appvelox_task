import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .models import Task
from .tools import \
    get_message_from_exception, \
    todo_response


def index(request):
    return HttpResponse('Hello, ToDo!')


def get_all_tasks(request):
    try:
        tasks = Task.objects.all()
        tasks_json = serializers.serialize(format='json', queryset=tasks)
        response = JsonResponse(
            status=200,
            data=tasks_json,
            safe=False
        )
        return todo_response(
            response=response,
            message='all tasks listed'
        )
    except Exception as ex:
        return todo_response(
            response=HttpResponse(status=500),
            message=get_message_from_exception(ex)
        )


@csrf_exempt
def create_new_task(request):
    try:
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

    except (json.decoder.JSONDecodeError, KeyError):
        return todo_response(
            response=HttpResponse(status=400),
            message='json doesn\'t exists or invalid'
        )

    except Exception as ex:
        return todo_response(
            response=HttpResponse(status=500),
            message=get_message_from_exception(ex)
        )


def get_task_by_id(request):
    try:
        pk = json.loads(json.loads(request.body))['pk']
        task = Task.objects.get(pk=pk)
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

    except (json.decoder.JSONDecodeError, KeyError):
        return todo_response(
            response=HttpResponse(status=400),
            message='json doesn\'t exists or invalid'
        )

    except Task.DoesNotExist:
        return todo_response(
            response=HttpResponse(status=403),
            message='task with id={} does not exist'.format(pk)
        )

    except Exception as ex:
        return todo_response(
            response=HttpResponse(status=500),
            message=get_message_from_exception(ex)
        )
     

@csrf_exempt
def complete_task_by_id(request):
    try:
        json_object = json.loads(json.loads(request.body))
        pk = json_object['pk']
        completion_date = json_object['completion_date']
        task = Task.objects.get(pk=pk)
        
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
    
    except (json.decoder.JSONDecodeError, KeyError):
        return todo_response(
            response=HttpResponse(status=400),
            message='json doesn\'t exists or invalid'
        )
    
    except Task.DoesNotExist:
        return todo_response(
            response=HttpResponse(status=403),
            message='task with id={} does not exist'.format(pk)
        )
    
    except Exception as ex:
        return todo_response(
            response=HttpResponse(status=500),
            message=get_message_from_exception(ex)
        )


@csrf_exempt
def delete_task_by_id(request):
    try:
        pk = json.loads(json.loads(request.body))['pk']
        task = Task.objects.get(pk=pk)
        task.delete()
        return todo_response(
            response=HttpResponse(status=200),
            message='task with id={} deleted'.format(pk)
        )
    
    except (json.decoder.JSONDecodeError, KeyError):
        return todo_response(
            response=HttpResponse(status=400),
            message='json doesn\'t exists or invalid'
        )
    
    except Task.DoesNotExist:
        return todo_response(
            response=HttpResponse(status=403),
            message='task with id={} does not exist'.format(pk)
        )
    
    except Exception as ex:
        return todo_response(
            response=HttpResponse(status=500),
            message=get_message_from_exception(ex)
        )
