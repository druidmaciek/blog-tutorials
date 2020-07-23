from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    title = models.CharField(max_length=75)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='lists')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Task(models.Model):
    parent_list = models.ForeignKey(List,
                                    on_delete=models.CASCADE,
                                    related_name='tasks')
    title = models.CharField(max_length=75)
    completed = models.BooleanField(default=False,
                                    blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
