from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    list_id = 0

    def __str__(self):
        return self.title