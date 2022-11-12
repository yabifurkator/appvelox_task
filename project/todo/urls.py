from django.urls import path

from .views import \
    get_all_tasks, \
    create_new_task, \
    get_task_by_id, \
    complete_task_by_id, \
    delete_task_by_id

urlpatterns = [
    path(route='all/', view=get_all_tasks),
    path(route='new/', view=create_new_task),
    path(route='get/', view=get_task_by_id),
    path(route='complete/', view=complete_task_by_id),
    path(route='delete/', view=delete_task_by_id)
]
