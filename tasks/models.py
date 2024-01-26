from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def created_at_display(self):
        return self.created_at.strftime('%b %e %Y')