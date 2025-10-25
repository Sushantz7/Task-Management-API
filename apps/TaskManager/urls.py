from django.urls import path

from .views import ProjectListView, ProjectCreateView

urlpatterns = [
    path("", ProjectListView.as_view(), name="list-project"),
    path("project/create/", ProjectCreateView.as_view(), name="create-project"),
]
