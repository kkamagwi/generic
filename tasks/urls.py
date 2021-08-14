from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDetailGenericView, TaskUpdateGenericView, TaskDestroyGenericView
# from tasks.views import TaskAPIView, TaskDetailAPIView, SetFinishedTaskAPIView


urlpatterns = [
    path('', TaskListView.as_view()),
    path('creation/', TaskCreateView.as_view()),
    path('<int:id>/', TaskDetailGenericView.as_view()),
    path('<int:id>/update/', TaskUpdateGenericView.as_view()),
    path('<int:id>/delete/', TaskDestroyGenericView.as_view()),
#     path('tasks/', TaskAPIView.as_view()),
#     path('tasks/<int:id>/', TaskDetailAPIView.as_view()),
#     path('tasks/<int:id>/finished/', SetFinishedTaskAPIView.as_view()),
]