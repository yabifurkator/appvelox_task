import json
from django.http import HttpResponse

from .tools import todo_response, get_message_from_exception


def common_exceptions_handling_endpoint(get_response):
    def middleware(request):
        try:
            response = get_response(request)
            return response
        
        except (json.decoder.JSONDecodeError, KeyError, ValueError):
            return todo_response(
                response=HttpResponse(status=400),
                message='json doesn\'t exists or invalid'
            )
 
        except Exception as ex:
            return todo_response(
                response=HttpResponse(status=500),
                message=get_message_from_exception(ex)
            )

    return middleware
