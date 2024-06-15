from . import views
from django.urls import path
from .views import TaskgetAPIView, TaskputAPIView, TaskpostAPIView, UserRegistrationView, Taskget_idAPIView, \
    TaskdeleteAPIView, TaskupdateAPIView

urlpatterns = [
    path('api/v1/tasklist/', TaskgetAPIView.as_view()),               # Все задачи
    path('api/v1/taskget/<int:pk>', Taskget_idAPIView.as_view()),     # Получение задачи по id
    path('api/v1/taskpost/', TaskpostAPIView.as_view()),              # Создать задачу
    path('api/v1/taskdelete/<int:pk>', TaskdeleteAPIView.as_view()),  # Удалить задачу по id
    path('api/v1/taskupdate/<int:pk>', TaskupdateAPIView.as_view()),  # Обновить задачу по id
    path('api/v1/register/', UserRegistrationView.as_view()),         # Регистрация
    path('api/v1/taskput/<int:pk>', TaskputAPIView.as_view()),        # CRUD

]
