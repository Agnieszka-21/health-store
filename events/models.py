from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    speaker = models.CharField(max_length=254)
    participants = models.ManyToManyField(User, blank=True, related_name='event')
    when = models.DateTimeField()
    registration_open = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)

    def __str__(self):
        if self.cancelled is False:
            string = f"{self.when} | {self.title}"
            return string
        else:
            return f"CANCELLED: {self.when} | {self.title}"
