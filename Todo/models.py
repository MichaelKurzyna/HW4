from django.db import models
from django.utils import timezone


class Todo(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.localtime)

