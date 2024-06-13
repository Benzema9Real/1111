from . import views
from django.urls import path
from .views import TaskgetAPIView,TaskputAPIView,TaskpostAPIView

urlpatterns = [
    path('api/v1/tasklist/', TaskgetAPIView.as_view()),
path('', TaskputAPIView.as_view()),
path('api/v1/taskpost/', TaskpostAPIView.as_view()),




]
