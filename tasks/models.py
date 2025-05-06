from django.db import models
from enum import Enum

PRIORITY_CHOICES = [
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High"),
]

# Create your models here.
class Task(models.Model):
    taskName=models.CharField(max_length=255)
    dueDate=models.IntegerField()
    priority=models.CharField(max_length=10,choices=PRIORITY_CHOICES)
    isCompleted=models.BooleanField(default=False)

    def __str__(self):
        return self.taskName