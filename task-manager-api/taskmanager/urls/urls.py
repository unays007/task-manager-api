from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskmanager.views import TaskViewSet, CategoryViewSet, RegisterView

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]
