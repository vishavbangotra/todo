from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True)
