from django.urls import include, path
from rest_framework.routers import DefaultRouter

from subjects.views import SubjectViewSet

router = DefaultRouter()

router.register("subjects", SubjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
