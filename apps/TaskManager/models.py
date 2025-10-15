from django.db import models
from django.contrib.auth import settings

from utils.base_model import BaseModel
from utils.constants import StatusChoices


class Project(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_projects",
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="member_projects"
    )

    def __str__(self):
        return self.name


class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    status = models.CharField(
        max_length=11, choices=StatusChoices, default=StatusChoices.TODO
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assigned_tasks",
    )

    def __str__(self):
        return self.title


class Comment(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()

    def __str__(self):
        return f"{self.author.email} commented on {self.task.title}"
