from django.http import HttpResponse


def get_message_from_exception(ex):
    return type(ex).__name__ + ': ' + str(ex)


def todo_response(response, message):
    response['message'] = message
    return response
