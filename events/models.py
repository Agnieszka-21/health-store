from django.db import models

from profiles.models import UserProfile


class Event(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    speaker = models.CharField(max_length=254)
    participants = models.ManyToManyField(UserProfile, related_name='event')
    when = models.DateTimeField()
    registration_open = models.BooleanField(default=False)

    class Meta:
        ordering = ["-when"]

    def __str__(self):
        return f"{self.when} | {self.title}"