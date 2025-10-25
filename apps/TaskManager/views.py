from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Project
from .serializers import ProjectSerializer, ProjectCreateSerializer


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
