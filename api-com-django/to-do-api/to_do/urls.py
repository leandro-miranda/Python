from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from to_do.views import UserViewSet, TaskViewSet

router = routers.DefaultRouter()

router.register(r"users", UserViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
