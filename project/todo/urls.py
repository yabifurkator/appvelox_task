from django.urls import path

from .views import \
    get_all_tasks_endpoint, \
    create_new_task_endpoint, \
    get_task_by_id_endpoint, \
    complete_task_by_id_endpoint, \
    delete_task_by_id_endpoint

urlpatterns = [
    path(route='all/', view=get_all_tasks_endpoint),
    path(route='new/', view=create_new_task_endpoint),
    path(route='get/', view=get_task_by_id_endpoint),
    path(route='complete/', view=complete_task_by_id_endpoint),
    path(route='delete/', view=delete_task_by_id_endpoint)
]
