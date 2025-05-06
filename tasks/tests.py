from django.test import TestCase
from .models import Task
# Create your tests here.


class TaskModelTest(TestCase):
    def test_create_task(self):
        task=Task.objects.create(
            taskName="Sample Task",
            dueDate=17400000,
            isCompleted=False
        )
        self.assertEqual(task.taskName,"Sample Task")
        self.assertFalse(task.isCompleted)