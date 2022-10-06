from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reticules.views import ReticuleModelViewSet

router = DefaultRouter()

router.register("reticules", ReticuleModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
