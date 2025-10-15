from django.db.models import TextChoices


class StatusChoices(TextChoices):
    TODO = "todo", "Todo"
    IN_PROGRESS = "in_progress", "In Progress"
    DONE = "done", "Done"
