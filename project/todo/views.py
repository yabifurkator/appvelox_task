from rest_framework.decorators import api_view
from .decorators import common_exceptions_handling_endpoint

from .endpoints_impl import \
    get_all_tasks_endpoint_impl, \
    create_new_task_endpoint_impl, \
    get_task_by_id_endpoint_impl, \
    complete_task_by_id_endpoint_impl, \
    delete_task_by_id_endpoint_impl


@api_view(['GET'])
@common_exceptions_handling_endpoint
def get_all_tasks_endpoint(request):
    return get_all_tasks_endpoint_impl(request=request)


@api_view(['POST'])
@common_exceptions_handling_endpoint
def create_new_task_endpoint(request):
    return create_new_task_endpoint_impl(request=request)


@api_view(['GET'])
@common_exceptions_handling_endpoint
def get_task_by_id_endpoint(request):
    return get_task_by_id_endpoint_impl(request=request)


@api_view(['POST'])
@common_exceptions_handling_endpoint
def complete_task_by_id_endpoint(request):
    return complete_task_by_id_endpoint_impl(request=request)
    

@api_view(['POST'])
@common_exceptions_handling_endpoint
def delete_task_by_id_endpoint(request):
    return delete_task_by_id_endpoint_impl(request=request)
