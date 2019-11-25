from django.db import models
# from __future__ import unicode_literals

# Create your models here.
class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True, max_length=10)
    title = models.CharField(max_length=50)
    remind_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
