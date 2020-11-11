from django.db import models


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=30, blank=False)
    is_done = models.BooleanField(default=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.text