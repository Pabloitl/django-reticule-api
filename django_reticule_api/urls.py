from django.urls import include, path


urlpatterns = [
    path("api/", include("reticules.urls")),
    path("api/", include("subjects.urls")),
]
