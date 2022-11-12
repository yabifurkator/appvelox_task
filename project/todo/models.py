from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    completion_date = models.DateField(null=True)
    completed = models.BooleanField(default=False)
