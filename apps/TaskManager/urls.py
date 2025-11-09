from django.urls import path

from .views import ProjectListView, ProjectCreateView, ProjectDetailAPIView

urlpatterns = [
    path("", ProjectListView.as_view(), name="list-project"),
    path("project/create/", ProjectCreateView.as_view(), name="create-project"),
    path(
        "project/<uuid:project_id>/",
        ProjectDetailAPIView.as_view(),
        name="project-detail",
    ),
]
